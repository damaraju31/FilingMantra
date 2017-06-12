from flask import Flask, render_template, request, make_response, jsonify, url_for, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'prodList'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/prodList'

mongo = PyMongo(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Notfound'}), 404)


@app.route('/success/<Pid>', methods=['POST'])
def success(Pid):
    result = request.form
    categories = str(result['categories']).lower()
    tags = str(result['tags']).lower().split(',')
    price = int(result['price'])
    name = str(result['name'])
    discount = int(result['discount'])
    quantity = int(result['quantity'])
    Id = int(Pid)
    mongo.db.product.update({'SKU_id': Id}, {
        '$set': {'name': name, "categories": categories, "tags": tags, "price": price, "discount": discount,
                 "quantity": quantity}})
    return redirect(url_for('product_list'))


@app.route('/')
def home_page():
    return render_template('form.html')


@app.route('/api/v1/products.json', methods=['POST'])
def products():
    result = request.form
    categories = str(result['categories']).lower()
    print categories
    tags = str(result['tags']).lower().split(',')
    price = result['price']
    if len(tags) == 1 and tags[0] == "":
        prd_list = mongo.db.product.find({"price": {'$lte': int(price)}, "categories": {'$in': categories.split()}},
                                         {'_id': 0})
    else:
        prd_list = mongo.db.product.find(
            {"price": {'$lte': int(price)}, "categories": {'$in': categories.split()}, "tags": {'$in': tags}},
            {'_id': 0})
    return render_template('output.html', prd_list=prd_list)


@app.route('/admin/products')
def product_list():
    product_list = mongo.db.product.find()
    return render_template('result.html', product_list=product_list)


@app.route('/admin/products/<item>')
def update_product(item):
    product_info = mongo.db.product.find({"SKU_id": int(item)})
    return render_template('update.html', product_info=product_info)


if __name__ == '__main__':
    app.run(debug=True)
