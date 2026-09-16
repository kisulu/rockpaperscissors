import random

number_to_guess = random.randint(1, 100)

while True:
	try:
		guess = int(input('Enter a number between 1 to 100: '))
		if guess > number_to_guess:
			print('Too High')

		elif guess < number_to_guess:
			print("Too Low")
		
		else: 
			print("Congratulations you guessed correctly")
			break
	except ValueError:
		print("Enter a valid number")

