'''
Coding Exercise 3
Section 3, Lecture 32
In exercise 1 you created a function that converted Celsius degrees to Fahrenheit.

The lowest possible temperature that physical matter can reach is -273.15 °C. With that in mind, please improve the function by making it print out a message in case a number lower than -273.15 is passed as input when calling the function.

'''


# Solution from exercise 1
celsius = input("Please enter a temperature (in celsius):")

def c_to_f(c):
    if float(c) < -237.15:
        return "That isn't even possible!"

    f = float(c) * 9 / 5 + 32
    return f

print(c_to_f(celsius))
