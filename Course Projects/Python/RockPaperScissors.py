import random

Player = 0
PlayerElection = ""

Computer = 0
ComputerElection = ""

EndGame = False
Error = False

Winner = ""

print("================")
print("Rock Paper Scissors")
print("================\n")

print("1) Rock ✊")
print("2) Paper 🤚")
print("3) Scissor ✌")

while EndGame == False:
    Player = int(input("\nPick a number: "))

    Computer = random.randint(1,3)

    #RESULTS!
    if Player == 1 and Computer == 2:
        Winner = "Computer"
        PlayerElection = "✊"
        ComputerElection = "✋"
    elif Player == 1 and Computer == 3:
        Winner = "Player"
        PlayerElection = "✊"
        ComputerElection = "✌"
    elif Player == 1 and Computer == 1:
        PlayerElection = "✊"
        ComputerElection = "✊"
    elif Player == 2 and Computer == 1:
        PlayerElection = "✋"
        ComputerElection = "✊"
        Winner = "Player"
    elif Player == 2 and Computer == 2:
        PlayerElection = "✋"
        ComputerElection = "✋"
    elif Player == 2 and Computer == 3:
        PlayerElection = "✋"
        ComputerElection = "✌"
        Winner = "Computer"
    elif Player == 3 and Computer == 1:
        PlayerElection = "✌"
        ComputerElection = "✊"
        Winner = "Computer"
    elif Player == 3 and Computer == 2:
        PlayerElection = "✌"
        ComputerElection = "✋"
        Winner = "Player"
    elif Player == 3 and Computer == 3:
        PlayerElection = "✌"
        ComputerElection = "✌"
    else:
        print("You entered a wrong number, try again!")
        Error = True

    if Winner:
        print(f"You chose: {PlayerElection}")
        print(f"CPU chose: {ComputerElection}")
        print(f"The {Winner} won!")
    else:
        if Error == False:
            print(f"You chose: {PlayerElection}")
            print(f"CPU chose: {ComputerElection}")
            print("It's a tie!")
    
    print("\nDo you want to end the game?")
    print("1) Yes")
    print("2) No")

    if int(input("Enter answer: ")) == 1:
        print("Thanks for playing!")
        EndGame = True
    else:
        print("Alright, go again!")
        Error = False
        Winner = ""
                