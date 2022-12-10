import json

def write_json(new_data, filename):
    with open(filename,'r+') as f:
        file_data = json.load(f)
        file_data["account"].append(new_data)
        f.seek(0)
        json.dump(file_data, f, indent = 4)

def body2dict(body):
    body = body.split("&")
    info = dict()
    for i in body:
        i = i.split("=")
        info.update({i[0]:i[1]})
    return info

def redirect(path):
    header = 'HTTP/1.1 302 OK\r\nContent-Type: text/html\r\n'
    location = 'Location: {}'.format(path)
    response = header + location
    return response

def main(body):
    info = body2dict(body)
    if(info["username"] == '' or info["password"] == ''):
        response = redirect('/SignUp.html')
    else:   
        with open('json/account.json','r+') as f:
            database = json.load(f)
        # print(database)
        if(len([i for i in database["account"] if i["username"] == info["username"]])):
            response = redirect('/SignUpError.html')
        else:
            write_json(info, 'json/account.json')
            response = redirect('/')
    
    return response
    
