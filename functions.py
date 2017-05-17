# Functions are used to encapsulate code blocks

# functions are defined using the def keyword, followed by a name
# and any data you want to pass to it in parentheses
def convert_to_dollars(rate, euros):
    dollars = euros * rate
    return dollars

print(convert_to_dollars(100, 1000))

# Using the return keyword, gives the item being returned, back to the code
# that calls it
def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

minutes = 30

# Here, we are using a function off of the string "object" called format, which
# replaces {0} with the first "argument", and {1} with the second, and so on
print("{0} minutes is equal to {1}".format(minutes, minutes_to_hours(minutes)))

# Here we are using default values, so the user isn't required to pass data
def minutes_to_hours_defaulted(minutes = 60, seconds = 0):
    hours = minutes / 60
    return hours

print("{0} minutes is equal to {1}"
      .format(minutes, minutes_to_hours_defaulted(minutes)))


# The type for a function that doesn't return anything has a different type than
# a function that does!

print(type(minutes_to_hours))

def no_return_function():
    print("doesn't return anything!")

print(type(no_return_function()))

# There is a function to get input from a user! Can you guess the funcions name?
age = input("Enter your age:") # returns a string, even if input is integer
print(type(age)) # Expected result: <class 'str'>
