shopping_cart_items = []

def average_price(cart_items):
    try:
        total_price = 0
        for item in cart_items:
            total_price += item.price

        average = total_price / len(cart_items)
    except ZeroDivisionError:
        average = 0

    return average

average_price_of_cart_items = average_price(shopping_cart_items)

print(f"Your average cart item price is {average_price_of_cart_items} dollars")