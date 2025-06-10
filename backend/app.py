from flask import Flask, jsonify
import socket

app = Flask(__name__)

products = [
    {"id": 1, "name": "Товар 1", "price": 100},
    {"id": 2, "name": "Товар 2", "price": 200}
]

@app.route('/api/products')
def get_products():
    print(f"Request served by {socket.gethostname()}")
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)