let Input = document.getElementById("myInput");
let messageBox = document.getElementById("messageBox");
let user
let Message = []
// let Onboard = []
let headers = {
    "Host": "linux10.csie.ntu.edu.tw:9090",
}

fetch('/active.json')
    .then((response) => {
        return response.json();
    })
    .then((response) => {
        user = response.username
    })
    .catch((error) => {
        console.log(`Error: ${error}`);
    })

fetch('/message.json')
    .then((response) => {
        return response.json();
    })
    .then((response) => {
        Message = response.message
        for (i = 10; i >= 1; i--) {
            if (Message.length - i < 0)
                continue;
            else {
                let message = document.createElement("div");
                message.className = "messageX";
                message.innerHTML = Message[Message.length - i].msg + " " + Message[Message.length - i].username;
                messageBox.appendChild(message);
            }
        }
    })
    .catch((error) => {
        console.log(`Error: ${error}`);
    })


function post() {
    if (Input.value) {
        let message = document.createElement("div");
        message.className = "messageX";
        message.innerHTML = Input.value + " " + user;
        body = { "username": user, "msg": Input.value }
        Input.value = "";
        messageBox.appendChild(message);
        fetch('/saveMsg.py', {
            method: "POST",
            headers: headers,
            body: JSON.stringify(body)
        })
    }
}

function logout() {
    
}