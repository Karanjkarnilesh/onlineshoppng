from flask import request
from flask_restful import Resource
from online_shopping_system.shopping_apis_service.food_service import food_delete_service, food_get_service, \
    food_put_service, food_post_service
from online_shopping_system.util.Food_dict_response import dict_response


class Food(Resource):
    def post(self):
        request_data = request.get_json()
        print("before ", request_data)
        object_food = food_post_service.create_food(request_data)
        if object_food:
            dict_response(object_food)
        else:
            return None

    def get(self, food_name=None):
        print("AT put food", food_name)
        if food_name:
            food_get_service.get_food(food_name)

    def put(self, food_name=None):
        print("AT put food", food_name)
        if food_name:
            food_put_service.update_food(food_name)
            print("Food details is update!!!!!!!!!")
    def delete(self,food_name):
        if food_name:
            food_delete_service.delete_food(food_name)