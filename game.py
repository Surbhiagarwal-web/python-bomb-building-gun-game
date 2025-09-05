import random
print("Welcome to the game of rock, paper, scissors")

choices = ("rock", "paper", "scissors")
comp = random.choice(choices)
user = input("Enter your choice: ")

if comp == user:
    print("Both have entered the same choice")
    print("The game is draw")

if comp == "rock" and user == "paper":
    print("Computer chose rock")
    print("You win")

if comp == "rock" and user == "scissors":
    print("Computer chose rock")
    print("You lost")

if comp == "paper" and user == "scissors":
    print("Computer chose paper")
    print("You win")

if comp == "paper" and user == "rock":
    print("Computer chose paper")
    print("You lost")

if comp == "scissors" and user == "rock":
    print("Computer chose scissors")
    print("You win")

if comp == "scissors" and user == "paper":
    print("Computer chose scissors")
    print("You lost")