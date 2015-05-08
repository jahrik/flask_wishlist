from flask import Flask
from flask import render_template
from wishlist import Wishlist

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    wishlist = Wishlist()
    # items = wishlist.get_list()
    items = wishlist.total_count()
    total = wishlist.total_cost()
    # return render_template('index.html', num_item=len(items), total=total)
    return render_template('index.html', num_item=items, total=total)


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
