document.getElementById('loadProducts').addEventListener('click', async () => {
    const response = await fetch('/api/products');
    const products = await response.json();
    document.getElementById('products').innerHTML = products.map(p => `<p>${p.name}: ${p.price} руб.</p>`).join('');
});