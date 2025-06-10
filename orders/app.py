from flask import Flask, request

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def create_order():
    order = request.json
    with open('/data/orders.txt', 'a') as f:
        f.write(f"{order}\n")
    return {"status": "success"}, 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)