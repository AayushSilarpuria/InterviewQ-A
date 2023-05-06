price = {"Apple": 34, "Banana": 4, "Papaya": 45, "Peach": 65,
         "Pomegranate": 50, "Pineapple": 45, "Strawberries": 5}
my_purchase = {"Apple": 2, "Banana": 4,
               "Papaya": 2, "Peach": 6, "Strawberries": 10}

Result = {}
for item in my_purchase:
    Result[item] = my_purchase[item] * price[item]

print(Result)
# output: {'Apple': 68, 'Banana': 16, 'Papaya': 90, 'Peach': 390, 'Strawberries': 50}

"""you can iterate through the my_purchase dictionary, multiply the corresponding values 
    with the prices from the price dictionary and store the result in a new dictionary Result."""
