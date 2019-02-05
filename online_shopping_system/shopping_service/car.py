from flask_restful import Resource, request
from online_shopping_system.util.Car_dict_response import car_response
from online_shopping_system.shopping_apis_service.car_service import car_delete_service, car_get_service, \
    car_post_service, car_put_service


class Car(Resource):
    def post(self):
        request_data = request.get_json()
        car_object = car_post_service.create_car(request_data)
        if car_object:
            car_response(car_object)
        else:
            return None

    def get(self, car_name=None):
        if car_name:
            print ("Car_Details")
            car_get_service.get_car(car_name)

    def put(self, car_name=None):
        if car_name:
            print ("Car_Details")
        car_put_service.update_car(car_name)
        print("Successfully updata!!!!")


    def delete(self, car_name=None):
        print("AT deletee ", car_name)
        if car_name:
            car_delete_service.delete_car(car_name)
            print("Car is DELETED!!!!")
