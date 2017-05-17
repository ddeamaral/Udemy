'''Coding Exercise 1
Section 3, Lecture 26
Please create a function that converts Celsius degrees to Fahrenheit.

Note: This is the first exercise of the course. Please try to complete this
and the rest of the exercises using the knowledge you have gained that far in
the course. The next lecture following each exercise contains the exercise
solution.

####----Google results for celsius to farenheit formula (0 celsius == 32 farenheit)----####
'''



# Solution
celsius = input("Please enter a temperature (in celsius):")

def c_to_f(c):
    f = c * 9 / 5 + 32
    return f

print(c_to_f(celsius))
