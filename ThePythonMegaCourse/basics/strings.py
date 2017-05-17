# There is a type in Python called string, like most languages
print(type("Hello World")) # prints out <class 'str'> since that is a class of string


#---- String indexing (Don't forget indexes start from 0) ---#
hello_world = "Hello world, how are you doing?"

# gets the characters from index 1 to index 5 getting 'ello'
ello = hello_world[1:5]

# prints ello
print(ello)

# I want to get the last character! Use character indexing
question_mark = hello_world[-1:]

# Alternatively, you can do this to get the question mark
# len is a 'function' that returns the length of whatever you pass to it
alt_question_mark = hello_world[len(hello_world) - 1]

print(alt_question_mark)

# prints '?'
print(question_mark)
