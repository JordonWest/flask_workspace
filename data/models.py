from peewee import *
import pathlib

path = f"{pathlib.Path().resolve()}/data/"
db = SqliteDatabase(f"{path}squid.db")

class Food(Model):
    name = CharField()
    rating = IntegerField()

    class Meta:
        database = db
db.connect()
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
