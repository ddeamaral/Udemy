# Dictionaries are just a list of key value pairs. The syntax is very similar
# to that of json

# Can be used to create a construct that is like a lookup table
my_first_dictionary = {"Name": "Dylan",
                       "Surname": "DeAmaral"}

# Notice that dictionaries are different than lists and tuples,
# in that they are access with the 'Key', in order to return the value
print(my_first_dictionary["Name"])

# The code below does not work. There is no key called 0!
# print(my_first_dictionary[0])

# You can store anything for values, even tuples and lists!
states_dictionary = {"State": "Massachusetts",
                     "Cities": ("Boston", "Framingham", "Cambridge"),
                     "Region": "New England"
                     }

# We can print out the tuple that is stored in the Cities key value pair!
print(states_dictionary["Cities"])

# If I wanted to get a city from the Cities, access it via index!
print(states_dictionary["Cities"][0])
