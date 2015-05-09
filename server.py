from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from wishlist import Wishlist

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def home():
    wishlist = Wishlist()
    items = wishlist.get_list()
    total_count = wishlist.total_count()
    total_types = wishlist.total_type()
    total = wishlist.total_cost()

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']
        if not name or not quantity or not price:
            flash('Please go fuck yourself!')
        else:
            item = {'name': name, 'quantity': quantity, 'price': price}
            items.append(item)
            wishlist.write_csv(items)
    else:
        pass

    return render_template('index.html', type_item=total_types, num_item=total_count, total=total)


@app.route('/view')
def view():
    wishlist = Wishlist()
    items = wishlist.get_list()
    return render_template('view.html', items=items)


@app.route('/dan')
def awesome():
    return '<strong>Dan is great!</strong>'


@app.route('/people')
def people():
    couples = [
                {'first': 'Dan', 'middle': 'Lee', 'last': 'Daggett'},
                {'first': 'Chika', 'middle': '', 'last': 'Shimono'}
               ]
    return render_template('people.html', people=couples)


if __name__ == "__main__":
    app.run()
