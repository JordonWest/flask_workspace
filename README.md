# Flask Presentation

## Prequisites
- Python3 (>=3.6 preferred)

## Starting your own Flask Application
Clone down this repo
- ```git clone git@github.com:JordonWest/flask_present.git```
- ```cd flask_present```

Create a virtual environment and install requirements.
- ```python3 -m venv venv ; source venv/bin/activate```
- ```pip install -r requirements.txt```

Create a directory and main file for your new project. 
- ```mkdir APP_NAME```
- ```cd APP_NAME```
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
# export FLASK_APP=FILE_NAME.py
# I recommend keeping app.py as your main file
```

## Creating a Homepage
Use html files within a template directory to build a web page
- ```mkdir templates```
- ```cd templates```
- ```touch home.html```

To content to your home page, add the following to home.html:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>APP_NAME</title>
    <link rel="stylesheet" href="../static/style.css">
  </head>
  <body>
    <h1> HEY I'M THE HOME PAGE! </h1>
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


### References:
- https://flask.palletsprojects.com/en/1.1.x/quickstart/
- https://docs.peewee-orm.com/en/latest/peewee/quickstart.html
- https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/
