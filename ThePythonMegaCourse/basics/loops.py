# Loops

# a loop is a way to make a code block execute, repeatedly
# There are a few different ways to loop

# For Loops

# Example:
emails = ['me@gmail.com', 'you@hotmail.com', 'they@gmail.com']

# stores each email in email, and allows you to do something with each email
for email in emails:

    # looking for gmail in each email. Only prints emails with gmail in them
    if 'gmail' in email:
        print(email)


# While Loops

password = ''

# This will keep executing, until the password variable contains 'python123'
while password != 'python123':

    password = input("Enter Password:")# Get input for password, set to password

    if password == 'python123': # Check if it's 'python123'
        print('You are logged in!')
    else:
        print('Sorry, please try again!')



# How to iterate through multiple lists

names = ['james', 'john', 'jack']
email_domains = ['gmail', 'hotmail', 'yahoo']
# zip, returns a tuple of the current index of both lists
for i, j in zip(names, email_domains):
    print(i, j)
