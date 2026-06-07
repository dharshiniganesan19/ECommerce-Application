

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():

    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    return render_template(
        'home.html',
        products=products
    )

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():

    if request.method == 'POST':

        customer_name = request.form['customer_name']

        conn = sqlite3.connect('ecommerce.db')
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO orders
        (customer_name, product_name, quantity, status)
        VALUES (?, ?, ?, ?)
        """,
        (customer_name, 'Laptop', 1, 'Processing'))

        conn.commit()
        conn.close()

        return redirect('/orders')

    return render_template('checkout.html')

@app.route('/orders')
def orders():

    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    conn.close()

    return render_template('orders.html', orders=orders)

@app.route('/admin')
def admin():
    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)