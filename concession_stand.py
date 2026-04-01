#All Variables

menu = {"popcorn":3.00,
        "pizza": 5.99,
        "macaroni": 2.23,
        "steak": 7.99,
        "potatoes": 6.99,
        "tea": 2.00,
        "water": 1.99}

cart = []
total = 0

print("---------MENU---------")
for key, value in menu.items():
    print(f"{key.capitalize():10}: ${value:>.2f}")
print("----------------------")

while True:
    food = input("Select your food please (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is None:
        print("Your food is not being listed in the menu")
    elif menu.get(food) is not None:
        cart.append(food)
        print("Your food is being listed")

for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")