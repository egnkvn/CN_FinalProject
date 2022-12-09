import random
import socket
import time

def check_content_type(filename):
    if(filename.endswith('.js')):
        return 'application/x-javascript'
    elif(filename.endswith('.jpg')):
        return 'text/css'
    else:
        return 'text/html'

def handle_request(request):
    """Handles the HTTP request."""
    headers = request.split('\n')
    print(headers)
    method, filename, version = headers[0].split()
    if(method == 'GET'):
        if filename == '/':
            filename = '/index.html'
        try:
            fin = open('.'+filename)
            content = fin.read()
            fin.close()
            ctype = check_content_type(filename)
            response = 'HTTP/1.0 200 OK\n'+ 'Content-Type: {}\n\n'.format(ctype) + content
        except FileNotFoundError:
            response = 'HTTP/1.0 404 NOT FOUND\n\n404 NOT FOUND'
    # elif(method == 'POST'):

    return response


s = socket.socket()         # Create a socket object
host = socket.getfqdn() # Get local machine name
port = 9091
s.bind((host, port))        

print ('Starting server on', host, port)
print ('The Web server URL for this would be http://%s:%d/' % (host, port))

s.listen(5)                 


while True:
    # Establish connection with client.    
    c, (client_host, client_port) = s.accept()
    print ('Got connection from', client_host, client_port)

    req = c.recv(1000).decode() # should receive request from client. (GET ....)
    print(req)

    res = handle_request(req)
    # print(res)
    c.send(res.encode())
    # c.send('HTTP/1.0 200 OK\n'.encode())
    # c.send('Content-Type: text/html\n'.encode())
    # c.send('\n'.encode()) # header and body should be separated by additional newline
    # c.send(html.encode())
    c.close()