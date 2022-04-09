# Squid Inc
These are the steps I took to create the now multi-million dollar social mega-media website, Squid Inc.

## Prequisites
- Python3 (>=3.6 preferred)

## Starting your own Flask Application
These steps come nearly word-for-word from https://flask.palletsprojects.com/en/1.1.x/quickstart/ 

Clone down this repo
- ```git clone git@github.com:JordonWest/flask_workspace.git```
- ```cd flask_workspace```

Create a virtual environment and install requirements.
- ```python3 -m venv venv ; source venv/bin/activate```
- ```pip install -r requirements.txt```

Create a main file for your new project. 
- ```touch app.py```

Paste boilerplate into app.py.
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```
Start the application to see it run.

```flask run```
```
# If you want a different name for the main file, you'll need to set an environment variable: 
# export FLASK_APP=squid.py
# I recommend keeping app.py as your main file
```

## Creating a Homepage
Use html files within a template directory to build a web page
- ```mkdir templates```
- ```cd templates```
- ```touch home.html```

To add content to your home page, add the following to home.html:
```
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Squid Inc</title>
    <link rel="stylesheet" href="../static/style.css">
  </head>
  <body>
    <h1> Homepage of Squid Inc </h1>
  </body>
</html>
```

Let's add a few things to app.py to serve this new template. Let's import the ```render_template``` method from Flask, update the function name (doesn't matter as long as it's unique), and use the ```render_template``` method to direct calls to this endpoint to our new ```home.html``` template. 
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html'), 200
```

Now lets run it!
- ```flask run```

## Adding second page and establish navigation.
Before becoming the tech super-giant we are today, Squid Inc was first a simple 2 page application.. It had a home page listing Squid's favorite foods, and a detail page to add, edit, or delete foods. We'll now replicate exactly what it looked like before we bought Google. 

To help cut down on repeated code, we'll use blocks to seperate out some of the boilerplate. Let's do some slight refactoring alongside building out some new features. In templates, we'll add a base page to hold our ```<head>``` content.
- ```touch templates/base.html```
Add the following to base.html:
```
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Squid Inc</title>
    <link rel="stylesheet" href="../static/style.css">
  </head>
  <body>
    {% block content %}
    {% endblock %}
  </body>
</html>
```
Lets then condense home.html, and add a button to get us to the next page. There are a number of ways to handle navigation in Flask, as it's basically just serving up standard html pages. We'll keep navigation simple for now with anchor tags cleverly disguised as buttons. (This is how we saved on upfront costs so we could beat Facebook to market.) 
```
{% extends "base.html" %}
{% block content %}
  <h1> Homepage of Squid Inc </h1>
  <button type="text"><a href="/food_detail">Go To Food Detail</a></button>
{% endblock %}
```
We'll now create a quick mock-up for our detail page. It won't be doing much until we start passing some data in. 
- ```touch templates/food_detail.html```
Add the following so we can keep our pages seperated and let us do some back and forth navigation:
```
{% extends "base.html" %}
{% block content %}
  <h1> Food Detail Page </h1>
  <button type="text"><a href="/">Back to the Home Page</a></button>
{% endblock %}
```
Last, we'll need to build a route to direct us to the detail page. Back in app.py, let's add the following code to intercept GET requests to "/food_detail".
```
@app.route('/food_detail')
def detail_page():
    return render_template('food_detail.html'), 200
```
Let's run it and see what Squid Inc's site looked like before we started our rocket program. 
- ```flask run```

## Setting up models, databases, and PeeWee.
Our game-breaking website would be nothing without the data we collect, parse through, and discretely sell to various parties. We rely on a postgres database, and Flask's free-form model format. There are a number of great ORM's out there, but at Squid Inc, we prefer [PeeWee](https://www.reddit.com/r/Python/comments/4tnqai/comment/d5jyuug/?utm_source=share&utm_medium=web2x&context=3). 

Let's create a model directory and simple model.py file to store Squid's favorite foods. 
- ```mkdir data ; cd data ; touch models.py```

Within models.py, we'll use Peewee's [Quickstart Guide](https://docs.peewee-orm.com/en/latest/peewee/quickstart.html) to create and connect to our database, and build out our tables. (The 'recreate' function will re-build the tabels each time. This is nice for development, but we'll remove this before going to production.) 
```
from peewee import *
import pathlib

# I like to give the full path to where I want the sqlite db to live. 
path = f"{pathlib.Path().resolve()}/data/"
db = SqliteDatabase(f"{path}squid.db")

class Food(Model):
    name = CharField()
    rating = IntegerField()

    class Meta:
        database = db
db.connect()
db.create_tables([Food])
```
Let's get back to app.py, import our models and see our database get created. 
In app.py add: ```from data.models import Food```, then run: 
- ```flask run``` 
Notice our spiffy new database in models/ with a slick new table:
- ```sqlite3 data/squid.db .tables```

## Creating Endpoints and Routes
Moving back to our templates, we'll add forms and buttons to get this multi-million dollar site to a multi-billion dollar Monolithic web-application. 
Let's update our Homepage to provide us a list of Squid's favorite foods. I'll run some proprietary seed data taken straight from users like you just to give us something to look at as we build out these features. We'll pass that to home.html straight from our Endpoint using Peewee's lovely pythonic syntax, then display it on the page with some Jinja.
Add the following to models for now. We will drop our Food table and re-seed each time we start the application.
```
...continued...

db.drop_tables([Food])
db.create_tables([Food])

def seed_food():
    seed_food = [
        {'name': 'hamburger', 'rating': 10},
        {'name': 'lettuce', 'rating': 9},
        {'name': 'chimkin', 'rating': 10},
        {'name': 'raw potato', 'rating': 9}
    ]

    for food in seed_food:
        Food.create(name=food['name'], rating=food['rating'])
seed_food()
```

Let's go to app.py and get this seed data passed to our home.html. We'll update the route with the following: 
```
@app.route('/')
def home_page():
    foods = Food.select()
    return render_template('home.html', foods=foods), 200
```
Look at that gorgeous Peewee query.. We will now populate on our front page by updating the existing code with the following:
```
{% extends "base.html" %}
{% block content %}
  <h1> Homepage of Squid Inc </h1>
  <h3>List of Foods</h3>
  <ul>
    {% for food in foods %}
    <li>{{food.name}} = ({{food.rating}})   <a href="/food_detail/{{food.id}}">edit</a></li>
    </br>
    {% endfor %}
  </ul>
{% endblock %}
```
Let's see how we're looking!
- ```flask run```

Beautiful. Well, we can Read, so let's get to the good part and make this a full CRUD app. Moving fast now, but Squid Inc didn't build the re-invent the internet without burning out a few thousand young coder souls.. Back in ```app.py``` let's update our food_detail route to receive parameters, GET, and POST requests. *NOTE*: Raw HTML forms cannot send HTTP verbs beyond GET and POST, so we're going to have to get a little creative with our routes to keep this short and sweet. This is not very RESTful, but I want to keep Javascript out of the mix for now. Update ```app.py``` with the following: 
```
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
    if request.method == 'POST':
        food.name = request.form['name']
        food.rating = request.form['rating']
        food.save()
        return redirect('/')

@app.route('/food_detail/<id>/delete', methods=['POST'])
def detail_delete(id):
    food = Food.get(id=id)
    food.delete_instance()
    return redirect('/')
```
That's a bunch of new code.. Let's talk about it line by line. Our home_page method is now accepting POSTs in addition to GETs (which is the default). We want to perform different actions based on the type of the request. If the request is a POST, we are expecing a request.form object which we will use to create a new Food item using Peewee. 
Our detail page has gotten multiple big changes. The endpoint now accepts an item id, allowing us to serve item-specific templates. Since raw HTML isn't very RESTful, to just build another Endpoint for deleting. Any other POST requests will be treated much like a PUT, writing to the instance of Food in any case. Any requests that are not GETs will be handled, then redirected back to the appropriate page. 
Let's build out that functionality into our templates, and watch this app run the way it did before we patented the ocean. Update ```home.html``` with the following:
```
{% extends "base.html" %}
{% block content %}
  <h1> Homepage of Squid Inc </h1>
  <h3>List of Foods</h3>
  <ul>
    {% for food in foods %}
     <li>{{food.name}} = ({{food.rating}})   <a href="/food_detail/{{food.id}}">edit</a></li>
    </br>
    {% endfor %}
  </ul>
  <h3> Enter a New Food </h3>
    <form action="/" method="POST">
      <input type="text" name="name" placeholder="Name of food">
      <input type="text" name="rating" placeholder="Enter a number rating">
      <input type="submit" value="Submit">
    </form>
{% endblock %}
```
And let's update our food_detail.
```
{% extends "base.html" %}
{% block content %}
  <h1> Food Detail Page </h1>
  <form action="/food_detail/{{food.id}}" method="POST">
    <input type="text" name="name" value="{{food.name}}">
    <input type="text" name="rating" value="{{food.rating}}">
    <input type="submit" value="Submit">
  </form>
  <form action="/food_detail/{{food.id}}/delete" method="POST">
    <input type="submit" value="Delete {{food.name}}">
  </form>
  <button><a href="/">Back to the Home Page</a></button>
{% endblock %}
```

Let's see the final product!
- ```flask run```

At long last, we're ready to go public. Heroku is a great resource for deploying hobby apps for yourself due too it's ease of use and the number of options you have available without paying a dime. Once you've created an account on Heroku, instructions are provided for deploying your application. I want to do a little bit of pre-work real quick to save you a few google searches. 
Heroku relies on a Procfile to give it instructions on how to run your application. To make this as easy for Heroku to understand, we've got gunicorn in our requirements.txt, and will use some of it's syntax to help speak to Heroku. Make a file called ```run.py``` and insert the following code. This is what ```flask run``` is doing under the hood, but we want to be deliberate for Heroku, as well as specify an environment variable. 
```
import os
os.environ["FLASK_ENV"] = "production"
from app import app

if __name__ == "__main__":
  app.run()
```

Next, let's create our super complex ```Procfile```.
- ```echo 'web: gunicorn run:app' >> Procfile```

Make sure you push all your work up. (Probably should have been doing this the whole time..)

On to Heroku. Using the UI, let's hook up our app. Simply go to "New" and select "Create new app". Give it a name and continue. From here, you can interact with the heroku CLI or simply directly from github. I find the Heroku CLI to be very useful for debugging, so I'd recommend installing it. ```heroku logs --tail``` will really help you debug any issues found in the deployment. For this, we'll mainly be interacting with the UI. 
Select "Connect to Github", find your app once connected to Github, and select your deploy preferences. I really like the automatic deployment as it utilized web-hooks to re-deploy your app each time you make a commit - this is great for a development branch. 
Simply hit the 'manual deploy' button for now, and watch your app come up!

### References
- https://flask.palletsprojects.com/en/1.1.x/quickstart/
- https://docs.peewee-orm.com/en/latest/peewee/quickstart.html
- https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/
