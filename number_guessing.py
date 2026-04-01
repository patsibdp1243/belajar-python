import random
"""
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = int(input("Enter your guess : "))
    if guess == answer:
        print("You are correct")
        is_running = False
    elif guess < answer:
        print ("Your guess is to low")
        guesses += 1
    elif guess > answer:
        print("Your guess is to high")
        guesses += 1

print(f"Congratulations, youre total guess is {guesses}")"""

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

player = input("Enter a choice (rock, paper, scissors) : ").lower()

while player not in options:
    print("You have to chose one of the three options")
    player = input("Enter a choice (rock, paper, scissors) : ")

print(f"Player : {player}")
print(f"Computer : {computer}")

if player == computer:
    print("It's a tie")

elif player == "paper" and computer == "scissors":
    print("You Lose")

elif player == "paper" and computer == "rock":
    print("You win")

elif player == "rock" and computer == "paper":
    print("You lose")

elif player == "rock" and computer == "scissors":
    print("You win")

elif player == "scissors" and computer == "rock":
    print("You lose")

elif player == "scissors" and computer == "paper":
    print("You win")
