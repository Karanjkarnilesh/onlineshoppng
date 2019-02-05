def update_food(object, data):
    if 'food_name' in data:
        object.FOOD.F_Name = data['food_name']

    if 'food_price' in data:
        object.FOOD.F_Price = data['food_price']

    object.save()
