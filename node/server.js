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
            totMem = os.totalmem() / 1000000;
            freeMem = os.freemem() / 1000000;
            cpuCount = os.cpus().length;
            srvDay = os.uptime() / 86400;
            srvHrs = ((os.uptime() % 86400) / 3600);
            srvMin = (((os.uptime() % 86400) % 3600) / 60);
            srvSec = ((os.uptime() % 86400) % 3600) % 60;
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
             <p>Server Uptime: Days: ${srvDay.toFixed(0)}, Hours: ${srvHrs.toFixed(0)}, Minutes: ${srvMin.toFixed(0)}, Seconds: ${srvSec.toFixed(0)}</p>
             <p>Total Memory: ${totMem} MB</p>
             <p>Free Memory: ${freeMem} MB</p>
             <p>CPU's: ${cpuCount}</p>
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