"""
Make a Rock Paper Sissors game where the uses plays against a computer that randomly selects it's move giving it's input.
The game should tell who won each round and keep track of the score
The game has to repeat until the user types "quit"
"""

import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'user'
    else:
        return 'computer'
    
def main():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("Enter rock, paper, scissors or quit to exit: ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            user_score += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        
        print(f"Score - You: {user_score}, Computer: {computer_score}\n")
    
    print("Final Score:")
    print(f"You: {user_score}, Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
