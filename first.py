"""principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount : "))
    if principle <= 0:
        print("Principle cant be less or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate amount : "))
    if rate <= 0:
        print("Interest rate cant be less or equal to zero")

while time <= 0:
    time = float(input("Enter the time amount : "))
    if time <= 0:
        print("Time cant be less or equal to zero")
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")"""

num_pad = ( (1, 2, 3), 
            (4, 5, 6), 
            (7, 8, 9), 
            ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
