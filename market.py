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





if __name__ == "__main__":
    app.run(debug=True)