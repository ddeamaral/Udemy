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



file = open('example.txt', 'a') # appendable file


# Use with, to avoid having to explicitly call the close method

with open('example.txt', 'a+') as file:
    file.seek(0)
    print( file.read() )



# r opens a file for reading only. The file pointer is placed at the beginning
# of the file. This is the default mode.

# r+ Opens a file for both reading and writing. Pointer at beginning of file

#w open a file for write only. Overwrites if exists, creates if not.

# w+ open a file for both writing and reading

# a opens for appending to end of a file. pointer is at the end. if not exists
# creates

# a+ appending and reading. pointer at end of file, and creates if not exists
