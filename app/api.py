from flask import Flask, request, jsonify
from app.cupones import get_final_price

app = Flask(__name__)

@app.route('/api/price', methods=['POST'])
def calculate():
    data = request.get_json()
    base_price = data.get('base_price')
    coupon = data.get('coupon')
    tax_rate = data.get('tax_rate', 0.19)

    final = get_final_price(base_price, coupon, tax_rate)
    return jsonify({"final_price": final})

