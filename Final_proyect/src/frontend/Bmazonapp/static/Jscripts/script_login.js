document.addEventListener('DOMContentLoaded', (event) => {
    let URL_Services = "http://127.0.0.1:8080"
    let URL_DJango = "http://127.0.0.1:8000/Bmazon/"
    async function call_Login(){

        let login_data = {
            user_email: document.getElementById('useremail').value,
            password: document.getElementById('password').value
        }
        console.log(login_data)

        url_post = URL_Services + '/Login'

        try{
            const response = await fetch(url_post, {
                method: 'POST',
                headers:{
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': URL_DJango,
                    "Access-Control-Allow-Methods": "POST"
                },
                body: JSON.stringify(login_data)
            });
            const data = await response.json();
            console.log(data)

            window.location.href = 'http://127.0.0.1:8000/Bmazon/home'
        }catch(error){
            console.error('Error', error)
        }
    }

    document.getElementById('logout_button').addEventListener('click', function() {
        window.location.href = 'login.html'; 
    });
    document.getElementById('shoppingcart_button').addEventListener('click', function() {
        window.location.href = 'shopping_cart.html'; 
    });

});