import django
from flask import Flask
from flask_restful import Api
django.setup()

from online_shopping_system.shopping_service.ping import Ping
from online_shopping_system.shopping_service.book import Book
from online_shopping_system.shopping_service.food import Food
from online_shopping_system.shopping_service.car import Car

app = Flask(__name__)

api=Api(app,prefix="/")

api.add_resource(Ping , "ping/")
api.add_resource(Book , "book/","book/<string:book_name>")
api.add_resource(Food ,"food/","food/<string:food_name>")
api.add_resource(Car,"car/","car/<string:car_name>")

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=7020)