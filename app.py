app.py - Backend com Flask
python
Copiar código
from flask import Flask, request, jsonify
from models import db, Client, Product, Sale
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vendas.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Rota para registrar clientes
@app.route('/register_client', methods=['POST'])
def register_client():
    data = request.json
    new_client = Client(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Cliente registrado com sucesso'}), 201

# Rota para registrar produtos
@app.route('/register_product', methods=['POST'])
def register_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Produto registrado com sucesso'}), 201

# Rota para registrar vendas
@app.route('/register_sale', methods=['POST'])
def register_sale():
    data = request.json
    client = Client.query.get(data['client_id'])
    product = Product.query.get(data['product_id'])
    
    if product.stock >= data['quantity']:
        new_sale = Sale(client_id=client.id, product_id=product.id, quantity=data['quantity'], sale_date=datetime.datetime.now())
        product.stock -= data['quantity']
        db.session.add(new_sale)
        db.session.commit()
        return jsonify({'message': 'Venda registrada com sucesso'}), 201
    else:
        return jsonify({'message': 'Estoque insuficiente'}), 400

if __name__ == '__main__':
    app.run(debug=True)
