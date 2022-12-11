import json

def write_json(new_data, filename):
    with open(filename,'r+') as f:
        file_data = json.load(f)
        file_data["message"].append(new_data)
        f.seek(0)
        json.dump(file_data, f, indent = 4)

def main(body):
    data = json.loads(body)
    write_json(data, 'json/message.json')
    response = 'HTTP/1.0 200 OK'
    return response