"""import time

my_time = int(input("Enter time in seconds : "))

for x in range (my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times up") """
"""
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food} : $"))
        foods.append(food)
        prices.append(price)


print("----- YOUR CART -----")

for food in foods:
    print(food , end=" ")
    
print()
for price in prices:
    total += price

print(f"Your total is : {total}") """

fruits = ["apple", "orange", "dragonfruit" , "banana"]
vegetables = ["carrots" , "Potatoes" , "Kangkung"]
meats = ["chicken" , "fish" , "cow"]

groceries = [fruits,vegetables,meats]

print(groceries[1][2])