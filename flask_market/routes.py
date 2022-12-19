from flask_market import app
from flask import render_template

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/market')
def market_page():
    return render_template('market.html')

@app.route('/phones')
def phones_page():
    items = [
        {'id': 1, 'name': 'iPhone 14 pro', 'manufacturer': 'Apple', 'price': 57500},
        {'id': 2, 'name': 'iPhone SE', 'manufacturer': 'Apple', 'price': 8600},
        {'id': 3, 'name': 'Redmi Note 10', 'manufacturer': 'Xiaomi', 'price': 9999},
        {'id': 4, 'name': 'Mi 11i', 'manufacturer': 'Xiaomi', 'price': 20999},
        {'id': 5, 'name': 'Galaxy S10', 'manufacturer': 'Samsung', 'price': 9300},
        {'id': 6, 'name': 'Galaxy Fold 4', 'manufacturer': 'Samsung', 'price': 67500},
        {'id': 7, 'name': 'K61', 'manufacturer': 'LG', 'price': 8100},
        {'id': 8, 'name': 'Sony Xperia 1', 'manufacturer': 'Sony', 'price': 46199}
    ]
    return render_template('phone.html', items=items) 

@app.route('/laptops')
def laptops_page():
    items = [
        {'id': 1, 'name': 'MacBook Pro 16', 'manufacturer': 'Apple', 'price': 114999},
        {'id': 2, 'name': 'MacBook Air 13', 'manufacturer': 'Apple', 'price': 42999},
        {'id': 3, 'name': 'Acer Swift 3', 'manufacturer': 'Acer', 'price': 23999},
        {'id': 4, 'name': 'RedmiBook 15', 'manufacturer': 'Xiaomi', 'price': 19999},
        {'id': 5, 'name': 'Asus X515AE', 'manufacturer': 'ASUS', 'price': 21330}
    ]
    return render_template('laptop.html', items=items)

@app.route('/cameras')
def cameras_page():
    items = [
        {'id': 1, 'name': 'Sony Alpha A7', 'manufacturer': 'Sony', 'price': 79999},
        {'id': 2, 'name': 'Cyber-Shot DSC', 'manufacturer': 'Sony', 'price': 59999}
    ]
    return render_template('camera.html', items=items)

@app.route('/headphones')
def headphones_page():
    items = [
        {'id': 1, 'name': 'AirPods Pro', 'manufacturer': 'Apple', 'price': 4399},
        {'id': 2, 'name': 'Redmi Buds', 'manufacturer': 'Xiaomi', 'price': 699},
        {'id': 3, 'name': 'Galaxy Buds', 'manufacturer': 'Samsung', 'price': 2050},
        {'id': 4, 'name': 'Razer Nari Ultimate', 'manufacturer': 'Razer', 'price': 8599}
    ]
    return render_template('headphone.html', items = items)

@app.route('/tablets')
def tablets_page():
    items = [
        {'id': 1, 'name': 'iPad Pro 11', 'manufacturer': 'Apple', 'price': 41999},
        {'id': 2, 'name': 'iPad 12.9', 'manufacturer': 'Apple', 'price': 58999},
        {'id': 3, 'name': 'Galaxy Tab S8', 'manufacturer': 'Samsung', 'price': 56999},
        {'id': 4, 'name': 'Sony Xperia Tablet', 'manufacturer': 'Sony', 'price': 11999},
        {'id': 5, 'name': 'Asus vivo book 13', 'manufacturer': 'ASUS', 'price': 24999},
        {'id': 6, 'name': 'LG G Pad 10', 'manufacturer': 'LG', 'price': 8500}
    ]
    return render_template('tablet.html', items = items)