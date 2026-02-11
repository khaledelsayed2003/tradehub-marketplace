from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv("config/.env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)


# --- Models ---
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description= db.Column(db.String(length=1024), nullable=False)
    
    

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
    {'id': 4, 'name': 'Mouse', 'barcode': '987654321012', 'price': 40},
    {'id': 5, 'name': 'Monitor', 'barcode': '456123789654', 'price': 300},
    {'id': 6, 'name': 'Headphones', 'barcode': '321654987123', 'price': 120},
    {'id': 7, 'name': 'Webcam', 'barcode': '741852963456', 'price': 80},
    {'id': 8, 'name': 'USB Drive', 'barcode': '159357486213', 'price': 25},
    {'id': 9, 'name': 'External HDD', 'barcode': '852456963147', 'price': 200},
    {'id': 10, 'name': 'SSD', 'barcode': '951357852456', 'price': 180},
    {'id': 11, 'name': 'Gaming Chair', 'barcode': '753159852456', 'price': 350},
    {'id': 12, 'name': 'Desk Lamp', 'barcode': '456789123654', 'price': 60},
    {'id': 13, 'name': 'Router', 'barcode': '963258741852', 'price': 110},
    {'id': 14, 'name': 'Smart Watch', 'barcode': '357159456258', 'price': 250},
    {'id': 15, 'name': 'Tablet', 'barcode': '258456147369', 'price': 400},
    {'id': 16, 'name': 'Microphone', 'barcode': '159753258456', 'price': 140},
    {'id': 17, 'name': 'Speakers', 'barcode': '753951456852', 'price': 130},
    {'id': 18, 'name': 'Power Bank', 'barcode': '456852159753', 'price': 55},
    {'id': 19, 'name': 'Camera', 'barcode': '852159753456', 'price': 700},
    {'id': 20, 'name': 'Printer', 'barcode': '147258369852', 'price': 280},
    ]
    return render_template('market.html', items=items)
    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
