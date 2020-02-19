var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");


http.createServer(function(req, res){

if (req.url === "/"){
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(body);
        });
    }
    else if(req.url.match("/sysinfo")){
            myHostName=os.hostname();
            html= `
            <!DOCTYPE html>
            <html>
             <head>
             <title> Node JS Response </title>
             </head>
             <body>
             <h1>Hello!</h1>
             <p>Welcome to my node site </p>
             <p>Hostname: ${myHostName}</p>
             <p>IP: ${ip.address()}</p>
             <p>Server Uptime: </p>
             <p>Total Memory:  </p>
             <p>Free Memory: </p>
             </body>
             </html>`
             res.writeHead(200, {"Content-Type":"text/html"});
             res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 file not found at ${req.url}`); 
        }
}).listen(3000);

console.log("Server listening on port 3000");