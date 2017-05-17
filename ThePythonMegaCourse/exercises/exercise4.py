'''
Coding Exercise 4
Section 4, Lecture 39
Consider the following list:

temperatures=[10,-20,-289,100]

Then, iterate over the temperature converter function that you created in execise 3 and print out the following output.

50.0
-4.0
That temperature doesn't make sense!
212.0

'''

temperatures=[10,-20,-289,100]

def c_to_f(c):
    if float(c) < -237.15:
        return "That isn't even possible!"

    f = float(c) * 9 / 5 + 32
    return f

for temperature in temperatures:

    print(c_to_f(temperature))
