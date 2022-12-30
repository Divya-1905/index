var host = window.location.protocol +"//"+ window.location.host
let csrf_token = document.querySelector(['namemiddlewaretokens']).value
var email,password

function login(
    email = document.getElementById("email").value,
    password = document.getElementById("password").value
)
console.log(email)
console.log(password)
fetch('http://127.0.0.1:8000/accounts/login',{
    method: 'POST',
    body :({
        'email': email,
        'password': password
    }),
    headers: new Headers({
        'X-CSRFTokens': csrf_token,
        'content_type': 'application/json'
    })

}).then(res => res.json()).then(data => {console.log(data)})
