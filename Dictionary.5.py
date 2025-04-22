grocery_prices = {
    'apple': 2.5,
    'banana': 1.2,
    'orange': 3.0,
    'bread': 1.5
}

grocery_quantities = {
    'apple': 4,
    'banana': 6,
    'orange': 3,
    'bread': 2
}

total_bill = sum(grocery_prices[item] * grocery_quantities[item] for item in grocery_prices)

print("Total Bill:", total_bill)
