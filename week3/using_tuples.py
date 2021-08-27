my_tuple = (1, 2, 3, 4, 5)

# Access tuple values
print(my_tuple[0] + my_tuple[1])

# Modify tuple values:

# This can not be done. It will throw an error
""" my_tuple[3] = 1 """

# However, you can re-assign the value of the variable that is holding a tuple
my_tuple = (5, 4, 3, 2, 1)
print(my_tuple)
