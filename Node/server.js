const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require("ip");


var server = http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
}
  
  else if(req.url.match("/sysinfo")) {

//hostname
 myHostName=os.hostname();

//time
var time = os.uptime()
var day = Math.floor(time/86400)
var hr = Math.floor((time-(day*86400))/3600)
var min = Math.floor((time-((day*86400)+(hr*3600)))/60)
var sec = time-((day*86400)+(hr*3600)+(min*60))

//memory
var totalMem = os.totalmem() / 1000000
var tMemory = totalMem.toFixed(3)
var freeMem = os.freemem() / 1000000
var fMemory = freeMem.toFixed(3)

    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: Days: ${day}: Hours: ${hr}: Minutes: ${min}: Seconds: ${sec}  </p>
        <p>Total Memory: ${tMemory} MB</p>
        <p>Free Memory:  ${fMemory} MB</p>
        <p>Number of CPUs: ${ os.cpus().length} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
}

else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
});

server.listen(3000)
console.log("Server listening on port 3000");