from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

menu = pd.read_csv('menu_data.csv')

@app.route('/')
def index():
    return "Welcome to KFC API"

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu.to_dict(orient='records'))

@app.route('/place_order', methods=['POST'])
def place_order():
    order = request.json['order']
    total_cost = calculate_total(order)
    return jsonify({"order": order, "total_cost": total_cost})

def calculate_total(order):
    total = sum(menu.loc[menu['Deal'] == item, 'Price (in Rs.)'].values[0] for item in order)
    return total

if __name__ == '__main__':
    app.run(debug=True)
