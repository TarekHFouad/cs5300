# This program takes in a price and discount and calculates the new price

def calculate_discount(price, discount):
    return round(price - (price * discount/100), 2)