from online_shopping_system.db.shopping_model.models import FOOD
def delete_food(food_name):
    try:
        car_object=FOOD.objects.filter(C_Name=food_name).first()
        car_object.delete()
    except Exception as e:
        print e
        return None