def redirect(path):
    header = 'HTTP/1.1 302 OK\r\nContent-Type: text/html\r\n'
    location = 'Location: {}'.format(path)
    response = header + location
    return response

def main():
    response = redirect('/MsgBoard.html')
    return response