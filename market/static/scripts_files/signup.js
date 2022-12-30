var host = window.location.protocol+" //"+ window.location.host
var name,email,address,phone 
let csrf_token = document.querySelector(['namemilddwaretoken']).value
function get(){
    var name = document.getElementById('id_name').value
    var email = document.getElementById("id_email").value
    var addres = document.getElementById("id_address").value
    var phone = document.getElementById("id_phone").value
}
console.log(email,address,phone,name  )
fetch('http://127.0.0.1:9000/api/signup', {
    method: 'POST',
    body: JSON.stringify({'email':email,'phone':phone,'name':name}),
    headers: new Headers({
      'X-CSRFToken':csrf_token,
      'Content-Type': 'application/json'
    }),

  }).then(res => {

    return res.json()

  }).then(data => {
    console.log(data)
    
  })
  window.location.href = `${host}/login`
   