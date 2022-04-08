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
<!DOCTYPE html>
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

Let's add a few things to app.py to serve this new template:
```
from flask import render_template
```

Replace our return statement with this: 
```
return render_template('home.html'), 200
```

Now lets run it!
- ```flask run```

## Adding second page and establish navigation
Before becoming the tech super-giant we are today, Squid Inc first needed additional pages.
To help cut down on repeated code, we'll use blocks to seperate out some of the boilerplate. 
In templates, add a base page to hold our ```<head>``` content. 
- ```touch templates/base.html```
Add the following to base.html:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link rel="stylesheet" href="../static/style.css">
  </head>
  <body>
    {% block content %}
    {% endblock %}
  </body>
</html>
```
In templates, add a second page:
- ```touch templates/second_page.hmtl```
Add some boilerplate to help us recognize which page we are on. 
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Squid Inc</title>
    <link rel="stylesheet" href="../static/style.css">
  </head>
  <body>
    <h1> Page 2 of Squid Inc </h1>
  </body>
</html>
```


### References:
- https://flask.palletsprojects.com/en/1.1.x/quickstart/
- https://docs.peewee-orm.com/en/latest/peewee/quickstart.html
- https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/
