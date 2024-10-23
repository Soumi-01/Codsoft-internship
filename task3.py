import random

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    # Game options
    choices = ['rock', 'paper', 'scissors']
    
    # Function to determine the winner
    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "Computer wins!"
    
    # Main game loop
    while True:
        # Prompt user for their choice
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        elif user_choice not in choices:
            print("Invalid choice, please try again.")
            continue
        
        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner and display the result
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Update the scores
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        
        # Display the current score
        print(f"Score: You - {user_score}, Computer - {computer_score}")
        
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Final score:")
            print(f"You: {user_score}, Computer: {computer_score}")
            print("Goodbye!")
            break

# Call the play_game function
play_game()
