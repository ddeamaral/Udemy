import random, string

# The purpose of this script is to improve upon the text-generator app
# shown in the Python Mega Course. This is more dynamic, since it will
# allow you to choose as many different versions of your pattern as you'd like

try:
	print("\nWelcome to the text generator! We will generate random words based on what you would like!\nLet's get started!")
	number_of_iterations = int(input('How many different versions would you like of your text?'))
	number_of_letters = int(input("How many letters would you like your text to be?"))
	letters = []

	for i in range(number_of_letters):
		letter = input("What letter would you like? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter:")
		letters.append(letter)

except TypeError:
	print("Sorry, that's not a real number")


def generator(seq):
	vowels = 'aeiou'
	consonants = 'bcdfghjklmnpqrstvwxyz'
	name = ''

	for letter in seq:

		if letter == 'v':
			name = name + random.choice(vowels)
		elif letter == 'c':
			name = name + random.choice(consonants)
		elif letter == 'l':
			name = name +  random.choice(string.ascii_lowercase)
		else:
			name = name + letter

	return name

for i in range(number_of_iterations):
	print(generator(letters))
