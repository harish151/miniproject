function fetchData(){
  document.getElementById('error-message').style.display='none';
  document.getElementById('loader').style.display='block';
  document.getElementById('content').style.display='block';
  document.getElementById('result').innerText='';
  document.getElementById('suggestion').innerText='';
  fetch('/')
  .then(Response => Response.json())
  .then(data => {
    document.getElementById('loader').style.display='none';
    document.getElementById('content').style.display='none';
    document.getElementById('result').innerText=data.message; 
    document.getElementById('suggestion').innerText=data.message;
    })
}
