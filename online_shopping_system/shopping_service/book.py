from flask import request
from flask_restful import Resource
from online_shopping_system.shopping_apis_service.book_service import book_post_service


class Book(Resource):
    def post(self):
        request_data = request.get_json()
        book_object= book_post_service.create_book(request_data)
        if book_object:
            print("Succesfully Data inserted!!!!")
        else:
            return None

