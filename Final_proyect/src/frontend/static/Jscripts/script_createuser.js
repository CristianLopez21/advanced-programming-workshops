let URL_BASE = "http://localhost:8080"

async function createUser(){
    let data={
        id: 0,
        user_name: document.getElementById('username').value,
        password: document.getElementById('password').value,
        user_email: document.getElementById('useremail').value,
        phone: "12345678901",
        acces: true,
        addres: "No available",
        shoppinghistory: {
            id_:0,
            products: ["No available"],
            total: 0,
        },
        pay_methods:{
            customer_username: "No available",
            number: "No available",
            due_date: "No available",
            cvv: "No available",
            name: "No available",
        }
    };
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

document.getElementById('logout_button').addEventListener('click', function() {
    window.location.href = 'login.html'; 
});
document.getElementById('shoppingcart_button').addEventListener('click', function() {
    window.location.href = 'shopping_cart.html'; 
});