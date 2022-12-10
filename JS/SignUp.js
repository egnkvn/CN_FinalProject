var input = document.getElementById("password");
var button = document.getElementById("button")

function CheckEmpty(value) {
  if(input.value == "")
    alert("Password cannot be empty")
}

button.addEventListener("click", CheckEmpty);
