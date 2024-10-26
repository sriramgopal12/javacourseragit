from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"name": "Sample Product", "category": "Category1", "price": 10, "available": True}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
