# from flask import Flask, render_template, request, redirect, url_for, flash
# from flaskSQLAlchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
# db = SQLAlchemy(app)

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     description = db.Column(db.Text, nullable=False)
    
#     def __repr__(self):
#         return self.name

# @app.route('/')
# def index():
#     products = Product.query.all()
#     return render_template('index.html', products=products)

# @app.route('/product/<int:product_id>')
# def product_detail(product_id):
#     product = Product.query.get_or_404(product_id)
#     return render_template('product_detail.html', product=product)

# @app.route('/cart', methods=['GET', 'POST'])
# def cart():
#     if request.method == 'POST':
#         product_id = request.form['product_id']
#         product = Product.query.get(product_id)
#         # Perform necessary validation and data processing
        
#         # Add product to the cart (e.g., store in session or database)
        
#         flash('Product added to cart', 'success')
#         return redirect(url_for('cart'))
    
#     # Retrieve products from the cart and pass them to the template
    
#     return render_template('cart.html')

# if __name__ == '__main__':
#     app.run(debug=True)

a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 