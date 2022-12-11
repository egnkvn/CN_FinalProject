import random
import socket
import time
from module import login, signup, saveMsg

def check_content_type(filename):
    if(filename.endswith('.js')):
        return 'JS','application/x-javascript'
    elif(filename.endswith('.css')):
        return 'css','text/css'
    elif(filename.endswith('.json')):
        return 'json','application/json'
    else:
        return 'html','text/html'

def handle_request(request):
    """Handles the HTTP request."""
    headers = request.split('\n')
    method, filename, version = headers[0].split()
    if(method == 'GET'):
        if filename == '/':
            filename = '/index.html'
        try:
            ftype, ctype = check_content_type(filename)
            fin = open('{}'.format(ftype)+filename)
            content = fin.read()
            fin.close()   
            response = 'HTTP/1.0 200 OK\n'+ 'Content-Type: {}\n\n'.format(ctype) + content
        except FileNotFoundError:
            response = 'HTTP/1.0 404 NOT FOUND\n\n404 NOT FOUND'
    elif(method == 'POST'):
        body = headers[-1]
        if(filename == '/login.py'):
            response = login.main(body)
        elif(filename == '/signup.py'):
            response = signup.main(body)
        elif(filename == '/saveMsg.py'):
            response = saveMsg.main(body)   
    return response


s = socket.socket()     # Create a socket object
host = socket.getfqdn() # Get local machine name
port = 9090
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
    c.close()