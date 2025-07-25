from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
        data = json.load(f)
        # not sure whether the json file has either a list or a dict
        if isinstance(data, dict):
            products = data.get('products', [])
            return products if isinstance(products, list) else []
        elif isinstance(data, list):
            return data
        else:
            return []


def read_csv():
    products = []
    with open('products.csv', newline='', encoding='utf-8') as f:
        # create a DictReader obj which read each row as an OrderedDict
        reader = csv.DictReader(f)
        # iterate each row(dict) in the CSV file
        for row in reader:
            # construct a dict with keys id, name, category, price
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sqlite():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, category, price FROM products")
    # call fetchall() on the cursor to retrieve all rows returned by SELECT query
    # result is a list of tuple
    rows = cursor.fetchall()
    connection.close()

    products = []
    for row in rows:
        # construct a dict for each product using the tuple elements
        # because tuple is a immutable sequence, does not support access using str keys
        products.append({
            'id': int(row[0]),
            'name': row[1],
            'category': row[2],
            'price': float(row[3])
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
    elif source == 'sql':
        products = read_sqlite()
    else:
        error = 'Wrong source'
        return render_template('product_display.html', error=error)

    if product_id is not None:
        products = [
            product for product in products if product['id'] == product_id]
    if not products:
        error = 'Product not found'
    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
