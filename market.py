from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about/<username>')
def about(username):
    return f"""
    <h1>Welcome {username}!</h1>
    <p>TradeHub is a Flask-based marketplace where users can buy and sell items.</p>
    """

@app.route('/market')
def market():
    items = [
        {
            'id': 1,
            'name': 'Headphone',
            'price': 200,
            'barcode': '35709847938424'
        },
        {
            'id': 2,
            'name': 'Laptop',
            'price': 1500,
            'barcode': '26604980037453'
        },
        {
            'id': 3,
            'name': 'Keyboard',
            'price': 350,
            'barcode': '55004283040892'
        }
    ]
    
    return render_template('market.html', items=items)




if __name__ == "__main__":
    app.run(debug=True)