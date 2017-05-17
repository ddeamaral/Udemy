# Tuples are not lists, and they are immutable (can't change them)
# Have a niche scenario for use

# You can have any types, just like lists
my_first_tuple = ("First Value", 3, 5)

# Prints out values
print(my_first_tuple)

# Can be indexed similar to lists
print(my_first_tuple[-1])

# Tuples have much fewer methods than lists as shown below
print(dir(tuple))

print(dir(list))
