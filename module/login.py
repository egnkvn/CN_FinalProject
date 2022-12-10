import json

def redirect(path):
    header = 'HTTP/1.1 302 OK\r\nContent-Type: text/html\r\n'
    location = 'Location: {}'.format(path)
    response = header + location
    return response

def body2dict(body):
    body = body.split("&")
    info = dict()
    for i in body:
        i = i.split("=")
        info.update({i[0]:i[1]})
    return info

def main(body):
    info = body2dict(body)
    with open('json/account.json','r+') as f:
        database = json.load(f)
    if(len([i for i in database["account"] if i["username"] == info["username"]])):
        for i in database['account']:
            if(i["username"] == info["username"]):
                databaseinfo = i
                break
        if(info["password"] == databaseinfo["password"]):
            response = redirect('/MsgBoard.html')
        else:
            response = redirect('/')
    else:
        response = redirect('/')
    return response
    