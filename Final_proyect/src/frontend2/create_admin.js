URL_BASE = "http://127.0.0.1:8080"

async function create_admin(){
    let data = {
        id: 0,
        user_name: document.getElementById('username').value,
        password: document.getElementById('password').value,
        user_email: document.getElementById('useremail').value,
        phone: document.getElementById('phone').value,
        access: true
    }
    console.log(data)

    let url_post = URL_BASE + '/register/admin'

    try{
        const response = await fetch(url_post,{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': ["*"],
                "Access-Control-Allow-Methods": "POST"
            },
            body: JSON.stringify(data)
        } )
        const result = await response.json();
        window.location.href = 'home.html'
    }catch (error){
        console.error('Error:', error);
    }   
}

async function callMessage() {
    try {
        const response = await fetch(URL_BASE + '/hello');
        const data = await response.text();
        document.getElementById('result').textContent = data;
    } catch (error) {
        console.error('Error:', error);
    }
}