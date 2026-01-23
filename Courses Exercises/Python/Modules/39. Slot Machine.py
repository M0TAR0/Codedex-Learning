# Program that recreates a slot machine game.
import random

symbols = ['🍒',' 🍇', '🍉', '7️⃣']
finish_game = False
number_of_tries = 1

def play():
    results = random.choices(symbols, k=3)
    print(f"{results[0]} | {results[1]} | {results[2]}")
    if len(set(results)) == 1: #Checks if all the elements were the same
        print("Jackpot!💰")
        global finish_game
        global number_of_tries
        finish_game = True
        print("Number of tries: " + str(number_of_tries))
        number_of_tries = 0
    else:
        print("Thanks for playing")

#Repeated Games
play()
while finish_game == False:
    print("\nDo you want to keep playing?")
    answer = input("Y/N:  ")
    if answer.lower() == "n":
        finish_game = True
        print("Goodbye!")
    else:
        print("Good Luck!\n")
        number_of_tries += 1
    play()
        