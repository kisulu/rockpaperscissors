# Ask the user to make a choice
# If choice is invalid
# 	print an error
# Let the compueter to make a choice as well
# Print Choices (emojis)
# Determin the winner
# Ask the user if they want to continue
# if not
#	terminate

import random

## USER CONSTANTS
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

choices = ('r', 'p', 's')
computer_choice = random.choice(choices)

computers_win = 0
users_win = 0
ties = 0

while True:
	user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
	if user_choice != ROCK and user_choice != PAPER and user_choice != SCISSORS:
		print("Please enter a valid choice r is Rock, p is Paper, and s is Scissors")
	else:
		if user_choice == computer_choice:
			print("You have tied")
			ties += 1
		elif (user_choice == ROCK and computer_choice == PAPER) or (user_choice == SCISSORS and computer_choice == PAPER) or (user_choice == PAPER and computer_choice == ROCK):
			print("User Wins!")
			users_win = users_win + 1

		else:
			print(f"Computers choice is {computer_choice}") 
			print("Computer Wins!!!")
			computers_win += 1

	## Computer has to choose again
	computer_choice = random.choice(choices)

	print(f"User Win: {users_win}, Computer Win: {computers_win}, Ties: {ties}")	

