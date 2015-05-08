from flask import Flask
from flask import render_template
from wishlist import Wishlist

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    wishlist = Wishlist()
    items = wishlist.get_list()
    for item in items:
        items = wishlist.total_count()
        types = wishlist.total_type()
    total = wishlist.total_cost()
    return render_template('index.html', type_item=types, num_item=items, total=total)


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
