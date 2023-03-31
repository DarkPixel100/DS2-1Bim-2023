const http = require('http');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('ô droga');
});
server.listen(3000, () => {
    console.log('servidor aberto');
});