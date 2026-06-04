const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.listen(port, () => {
    console.log(`Node.js frontend listening at http://localhost:${port}`);
    console.log(`Open http://localhost:${port} in your browser to view the ChatGPT clone UI.`);
});
