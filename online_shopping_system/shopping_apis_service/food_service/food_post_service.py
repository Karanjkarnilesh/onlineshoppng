import django

django.setup()
from online_shopping_system.db.shopping_model.models import FOOD

def create_food(object_food):
    name = object_food["Name"]
    price = object_food["Price"]
    print("in create method",name,price)
    try:
        food_object= FOOD.objects.create(F_Name= name,
                                         F_Price = price)
        print("DATA ENTER")
        return food_object

    except Exception as e:
        print e
        return None