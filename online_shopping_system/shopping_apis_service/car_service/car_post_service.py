import django
from online_shopping_system.db.shopping_model.models import CAR
from datetime import date
django.setup()


def create_car(object):
    
    name = object["C_name"]
    price = object["C_price"]
    loanch = date.today()
    model = object["C_model"]
    try:
        car_object = CAR.objects.create(C_Name=name,
                                        C_Loanch=loanch,
                                        C_Price=price,
                                        C_Model=model,
                                        )
        print("DATA ENTER")
        return car_object

    except Exception as e :
        print e
        return None