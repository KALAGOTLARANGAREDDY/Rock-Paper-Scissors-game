import random

def play_game():
    while True:
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        player_choice = None
        
        while player_choice not in choices:
            player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        print(f"Player choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lost!")
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing! Bye!")

play_game()

