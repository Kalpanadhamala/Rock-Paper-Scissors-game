import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"] 
round_played = 0

while True:
    user_input = input("Enter Rock, Paper, Scissors or Q/quit: ").lower()
    if user_input == "q":  
        break
    else:
        computer_input = random.choice(options)  
        print(f"You chose: {user_input}, Computer chose: {computer_input}")
        
    if (user_input == "rock" and computer_input == "scissors") or\
     (user_input == "scissors" and computer_input == "paper") or\
     (user_input == "paper" and computer_input == "rock") :
         print("You won!")
    elif user_input == computer_input:
        print("It is tie")
    else:
         print("Computer won!")
    computer_wins += 1
        
    round_played += 1
    if round_played == 4:
        print(f"Game Over!, Final Score:\nYou: {user_wins},Computer: {computer_wins}")
    
        play_again = ("Do you want to play game again?(yes/no): ").lower()
        
        if play_again != "yes":
            print("Thanks for playing")
            break
        else:
           user_wins = 0
           computer_wins = 0
           rounds_played = 0
           print("Starting a new game...\n")