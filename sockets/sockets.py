import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "pythonprogramming.net"
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: " + server + "\n\n"

s.connect((server, port))
s.send(request.encode())

bufferSize = 4096
result = s.recv(bufferSize)

# iterate through parts of the buffered response
while len(result) > 0:
  print(result)
  result = s.recv(bufferSize)
