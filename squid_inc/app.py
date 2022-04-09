from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html'), 200

@app.route('/food_detail')
def detail_page():
    return render_template('food_detail.html'), 200
