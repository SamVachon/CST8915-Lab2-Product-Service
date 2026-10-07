import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Dog Food", "price": 19.99},
    {"id": 2, "name": "Cat Food", "price": 34.99},
    {"id": 3, "name": "Bird Seeds", "price": 10.99},
]


@app.get("/products")
def get_products():
    return jsonify(products)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "3030"))
    app.run(host="0.0.0.0", port=port)