URL_BASE = "http://localhost:8080"

async function showProducts(){
    try{
        const response = await fetch(URL_BASE + '/catalogue/products');
        const data = await response.json();

        let table = '<table>';
        table += '<tr><th>Name</th><th>Price</th><th>Description</th></tr>';
        
        data.forEach(item => {
            table += `<tr><td>${item.name}</td><td>${item.price}</td><td>${item.description}</td></tr>`;
        });
        
        table += '</table>';
        
        document.getElementById('Table').innerHTML = table;

    }catch (error) {
        console.error('Error:', error);
    }
}