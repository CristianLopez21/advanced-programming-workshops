let URL_BASE = "http://127.0.0.1:8080"

async function createUser(){
    let data={
        id: 0,
        user_name: document.getElementById('username').value,
        password: document.getElementById('password').value,
        user_email: document.getElementById('useremail').value,
        phone: "12345678901",
        access: true,
    }
    console.log(data)

    let url_post = URL_BASE + '/register/user'

    try{
        const response = await fetch(url_post, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': ["*"],
                "Access-Control-Allow-Methods": "POST"
            },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        document.getElementById('result').textContent = result.message;
    } catch (error) {
        console.error('Error:', error);
    }
    
}