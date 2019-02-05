
def update_car(object,data):

    if 'car_name' in data:
        object.CAR.C_Name=data['car_name']

    if 'car_model' in data:
        object.CAR.C_Model = data['car_model']

    if 'car_loanch' in data:
        object.CAR.C_Loanch = data['car_loanch']

    if 'car_price' in data:
        object.CAR.C_Price = data['car_price']

        object.save()



