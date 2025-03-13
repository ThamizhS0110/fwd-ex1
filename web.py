from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Powers of a Number</title>
    <script>
        function calculatePowers() {
            let num = document.getElementById("number").value;
            let result = "";
            for (let i = 1; i <= 10; i++) {
                result += `${num}^${i} = ${Math.pow(num, i)}<br>`;
            }
            document.getElementById("output").innerHTML = result;
        }
    </script>
</head>
<body>
    <h2>Calculate Powers of a Number (Up to 10)</h2>
    <label for="number">Enter a number:</label>
    <input type="number" id="number" value="2">
    <button onclick="calculatePowers()">Calculate</button>
    <div id="output"></div>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()