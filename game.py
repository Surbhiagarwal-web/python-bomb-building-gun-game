import random
print("Welcome to the game of Gun, Building, Bomb")

choices = ("Gun", "Building", "Bomb")
comp = random.choice(choices)
user = input("Enter your choice: ")

if comp == user:
    print("Both have entered the same choice")
    print("The game is draw")

if comp == "Bomb" and user == "Gun":
    print("Computer chose Bomb")
    print("You win")

if comp == "Bomb" and user == "Building":
    print("Computer chose Bomb")
    print("You lost")

if comp == "Building" and user == "Bomb":
    print("Computer chose Building")
    print("You win")

if comp == "Building" and user == "Gun":
    print("Computer chose Building")
    print("You lost")

if comp == "Gun" and user == "Bomb":
    print("Computer chose Gun")
    print("You lost")

if comp == "Gun" and user == "Building":
    print("Computer chose Gun")
    print("You Win")