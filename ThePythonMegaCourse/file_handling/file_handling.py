# File handling

# The purpose of this is how to read from files in python

# This is how you open a file. The second 'argument' is the mode you want
file = open('example.txt', 'r')

# _io.TextIOWrapper type
type(file)

# This retrieves the contents as a python string
content = file.read()
print(content)

# If you want to get the lines as a list from a file, use readlines().
# Printing this doesn't get you a list like you'd expect
content = file.readlines()
print(content)


# The reason is read, had left the pointer, at the end of the file.
# To go back to the beginning, use the seek() method
file.seek(0)
content = file.readlines()
print(content)

# To get the lines, without the newline characters (\n), do the following:
content = [i.rstrip('\n') for i in content]

# The above uses list comprehension, which generates a list. i is a temporary
# variable, like in for loops, and rstrip is a method that will strip characters
# from a string

print(content)


# How to write to a file
file = open('example.txt', 'w')
file.write('Line 1')

# note, this will create a new file, write the text to it, and overwrite what
# ever was in the file, and in the file system.
