from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import warnings
import os

warnings.filterwarnings("ignore")

app = FastAPI(title="Nexira IT Assistant API")

# Enable CORS for the Node.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, set this to the frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Configuration ---
MODEL_NAME = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTORSTORE_DIR = "vectorstore"

rag_chain = None

def initialize_rag():
    import torch
    from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
    from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
    from langchain_community.vectorstores.faiss import FAISS
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import RunnablePassthrough

    print("Loading Embeddings and Vectorstore...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    if not os.path.exists(VECTORSTORE_DIR):
        print(f"Error: {VECTORSTORE_DIR} not found. Run ingest.py first.")
        return None
        
    vectorstore = FAISS.load_local(
        VECTORSTORE_DIR, 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    print(f"Vectorstore loaded with {vectorstore.index.ntotal} vectors.")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    print("Loading LLM...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, 
        device_map="auto", 
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        trust_remote_code=True
    )

    # --- STRICT LENGTH ENFORCEMENT ---
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = model.config.eos_token_id

    # Configure model defaults
    model.generation_config.max_new_tokens = 1024
    model.generation_config.max_length = 4096 
    model.generation_config.temperature = 0.4
    model.generation_config.do_sample = True
    model.generation_config.repetition_penalty = 1.15
    model.generation_config.pad_token_id = model.config.pad_token_id
    model.generation_config.eos_token_id = model.config.eos_token_id

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        return_full_text=False,
    )

    # Pass parameters here to be 100% sure LangChain enforces them
    llm = HuggingFacePipeline(
        pipeline=pipe,
        pipeline_kwargs={
            "max_new_tokens": 1024,
            "max_length": 4096,
            "temperature": 0.4,
            "do_sample": True,
            "repetition_penalty": 1.15
        }
    )

    # 3. Define the Prompt (Strict ChatML Format for SmolLM2)
    template = """<|im_start|>system
You are a highly accurate Nexira IT Support Professional. Your sole purpose is to answer the user's query based EXCLUSIVELY on the provided Context. 

CRITICAL RULES:
- DO NOT invent, hallucinate, or guess any information.
- DO NOT provide historical background, URLs, or external knowledge that is not explicitly in the text.
- If the Context does not contain the answer, you MUST reply exactly: "I apologize, but our internal documentation does not contain information regarding that request."
- Be concise and use Markdown headers (###) and bullet points.<|im_end|>
<|im_start|>user
Context Information:
{context}

User Query:
{query}<|im_end|>
<|im_start|>assistant
"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "query"]
    )

    def format_docs(docs):
        print(f"\n--- DEBUG: RETRIEVED {len(docs)} CHUNKS ---")
        for i, doc in enumerate(docs):
            print(f"--- Chunk {i} ({doc.metadata.get('source', 'unknown')}) ---")
            print(f"{doc.page_content}\n")
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "query": RunnablePassthrough()}
        | prompt
        | llm
    )
    
    return chain

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Nexira IT Assistant API is running. Use /chat to interact with the RAG system."}

@app.on_event("startup")
def on_startup():
    global rag_chain
    rag_chain = initialize_rag()

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    if rag_chain is None:
        raise HTTPException(status_code=503, detail="RAG chain not initialized. Please ensure the vectorstore exists.")
    
    query = request.query
    print(f"\n--- NEW QUERY: {query} ---")
    
    try:
        # Run the chain
        answer = rag_chain.invoke(query)
        
        # Clean up output
        answer = answer.split("<|im_end|>")[0].strip()

        # Remove common hallucinated labels
        prefixes_to_remove = ["Answer:", "assistant:", "Assistant:", "IT Assistant:"]
        for prefix in prefixes_to_remove:
            if answer.startswith(prefix):
                answer = answer[len(prefix):].strip()

        if not answer or len(answer) < 5:
            answer = "I apologize, but I couldn't generate a clear answer from the current documentation. Could you please rephrase your question?"
            
        print(f"Final Answer: {answer[:100]}...\n")
        return ChatResponse(answer=answer)
    except Exception as e:
        print(f"ERROR in chat_endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
