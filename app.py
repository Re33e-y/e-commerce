from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
products = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Keyboard', 'price': 75}
]

@app.route('/')
def home():
    return "Welcome to the E-commerce Website!"

@app.route('/products')
def show_products():
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
