from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def display_item():
    with open('items.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        items = data.get('items', [])
    return render_template('items.html', items=items)


def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    products = []
    with open('products.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        error = 'Wrong source'

    if products and product_id is not None:
        products = [
            product for product in products if product['id'] == product_id]
    if not products and error is None:
        error = 'Product not found'
    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
