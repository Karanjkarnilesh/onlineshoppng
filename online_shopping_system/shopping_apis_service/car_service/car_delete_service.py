from online_shopping_system.db.shopping_model.models import CAR
def delete_car(car_name):
    try:
        car_object=CAR.objects.get(C_Name=car_name)
        car_object.delete()
    except Exception as e:
        print e
        return None
