# Create a list of words and randomly select one.
# Initialize variables to store guessed characters and remaining attempts.
# Display the word using underscores for unguessed characters.
# Accept a character from the user.
# Check whether the character exists in the word.
# Continue until the word is guessed or all attempts are exhausted.
# Display the result.

import random

list_of_words =["create", "list", "words", "and", "randomly", "select", "one"]

store_guessed = random.choice(list_of_words)
stored_char = tuple(store_guessed)

remaining_attempts=3
index_of_char = 0

name = input("What is your name? ")
print("Good Luck ! ", name)

while remaining_attempts > 0 and index_of_char < len(stored_char): 
	char_frm_user = input("Type: ").lower()

	if char_frm_user == stored_char[index_of_char]:
        	print("Correct!")
        	index_of_char += 1

	else:
		remaining_attempts -= 1
		print(f"Wrong character! Remaining attempts: {remaining_attempts}")


if index_of_char == len(stored_char):
    print(f"The word was: {store_guessed}")
    print("Congratulations! You spelled the word successfully.")
else:
    print(f"Game over! The word was: {store_guessed}")

