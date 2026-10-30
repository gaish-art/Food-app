from flask import Flask, render_template, request, redirect

app = Flask(__name__)

menu = [
    {"name": "Idli", "price": 20},
    {"name": "Dosa", "price": 40},
    {"name": "Parotta", "price": 50}
]

orders = []

@app.route('/')
def home():
    return render_template('home.html', menu=menu)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        item = request.form['item']
        orders.append(item)
        return redirect('/order')

    return render_template('order.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)