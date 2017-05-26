import random

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = vowels + consonants

length_of_text = input("How long would you like the random text to be?")
inputs = []

for i in range(int(length_of_text)):
	letter_input_1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")

	if letter_input_1 == 'v':
		inputs.append(random.choice(vowels))
	elif letter_input_1 == 'c':
		inputs.append(random.choice(consonants))
	elif letter_input_1 == 'l':
		inputs.append(random.choice(letters))
	else:
		inputs.append(letter_input_1)

def plot():
	for letter in inputs:
		

	if letter_input_2 == 'v':
		l2=random.choice(vowels)
	elif letter_input_2 == 'c':
		l2=random.choice(consonants)
	elif letter_input_2 == 'l':
		l2=random.choice(letters)
	else:
		l2=letter_input_2

	if letter_input_3 == 'v':
		l3=random.choice(vowels)
	elif letter_input_3 == 'c':
		l3=random.choice(consonants)
	elif letter_input_3 == 'l':
		l3=random.choice(letters)
	else:
		l3=letter_input_3
	name = l1+l2+l3
	return name

for i in range(10):
	print(plot())
