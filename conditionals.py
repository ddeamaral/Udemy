# Conditionals\

# A conditional is a way to control the flow of your program, using conditions
a = 5

# How do we do something, only if 5 is less than 5
if a < 5:
    print("less than 5")
    # do whatever else you'd want to

elif a == 5:
    # This runs if a < 5 does not run, and it happens to be 5. Otherwise go to
    # else statement
    print("is 5")

else:
    # do this if the (a < 5) condition is not minutes_to_hours
    print("greater than or equal to 5")

# Try changing the value of 5 to see the different code blocks get executed
