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

Create a directory and main file for your new project. 
- ```mkdir squid_inc```
- ```cd squid_inc```
- ```touch app.py```

Paste boilerplate into app.py.
```from flask import Flask
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
  <button type="text"><a href="/food_detail">Go To Page 2</a></button>
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




### References:
- https://flask.palletsprojects.com/en/1.1.x/quickstart/
- https://docs.peewee-orm.com/en/latest/peewee/quickstart.html
- https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/
