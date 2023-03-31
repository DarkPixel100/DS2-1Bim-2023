const http= require('http');
const fs = require('fs');

const server = http.createServer ((req,res) => {
    fs.readFile('index.html',(err, data) => {
        if (err) {
            res.writeHead(500, {'Content-Type':'text/plain'})
            res.end('Erro interno do servidor');
        } else {
            res.writeHead(200, { 'Content-Type': 'text/html' })
            res.end(data);
        }
    });
});
server.listen(3000, () => {
    console.log('rodou');
})
