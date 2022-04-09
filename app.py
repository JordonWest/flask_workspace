from flask import Flask, render_template, redirect, url_for, request
from data.models import Food

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home_page():
    if request.method == 'POST':
        Food.create(name=request.form['name'], rating=request.form['rating'])
        return redirect('/')
    else:
        foods = Food.select()
        return render_template('home.html', foods=foods), 200

@app.route('/food_detail/<id>', methods=['GET', 'POST'])
def detail_page(id):
    food = Food.get(id=id)
    if request.method == 'GET':
        return render_template('food_detail.html', food=food), 200
    elif request.method == 'POST':
        food.name = request.form['name']
        food.rating = request.form['rating']
        food.save()
        return redirect('/')

@app.route('/food_detail/<id>/delete', methods=['POST'])
def detail_delete(id):
    food = Food.get(id=id)
    food.delete_instance()
    return redirect('/')

