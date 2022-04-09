import os
os.environ["FLASK_ENV"] = "production"
from app import app

if __name__ == "__main__":
  app.run()
