from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'sua-chave-secreta-super-forte'
jwt = JWTManager(app)


products_db = [
    {
        "id": 1,
        "product_name": "Coleira",
        "product_description": "Coleira para cachorro de pequeno porte",
        "product_price": 23.90,
        "product_photo": "https://example.com/coleira.jpg",
        "stock_quantity": 26
    },

]



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login-page')
def login_page():
    return render_template('login.html')



@app.route('/api/login', methods=['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == 'admin':
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'error': 'Credenciais inválidas'}), 401



@app.route('/products-page')
@jwt_required()
def products_page():
    current_user = get_jwt_identity()
    return render_template('products.html', products=products_db)



@app.route('/api/products', methods=['GET'])
@jwt_required()
def get_products():

    pass


@app.route('/api/products/<int:product_id>', methods=['GET'])
@jwt_required()
def get_product(product_id):

    pass


if __name__ == '__main__':
    app.run(debug=True)