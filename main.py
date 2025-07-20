# import necessary libraries
import random

# win_loss logic function
def win_loss(player_input, computer_input):
    if(player_input == computer_input):
        print("Its a Tie")

    else:
        if(player_input == 1 and computer_input == 0):
            print("Congratulations, You win this round.")

        elif(player_input == 0 and computer_input == -1):
            print("Congratulations, You win this round.")

        elif(player_input == -1 and computer_input == 1):
            print("Congratulations, You win this round.")
        
        else:
            print("Computer wins this round")

# Making dictionary
choices = {
    "snake": 1,
    "water": 0,
    "gun": -1
    }

# Using loop for continue rounds
while(True):
    player_input = int(input("Enter a number '1' for 'snake', '0' for 'water', '-1' for 'gun': "))  # for player input
    computer_input = choices[random.choice(list(choices.keys()))]   # for computer random choice

    print(f"Your chose: {player_input}")
    print(f"Computer chose: {computer_input}")

    win_loss(player_input, computer_input)  # function call

    again = int(input("Enter '1' for continue playing and '0' for leave the game: "))   # for continue playing
    if(again != 1):
        break