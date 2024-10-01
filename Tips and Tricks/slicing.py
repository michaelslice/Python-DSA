my_list = [1, 2, 3, 4]
# Negative 1 is not out of bounds, this is the last element
print(my_list[-1])

# Negative 2 is the second to last value
print(my_list[-1])

# Sublists aka slicing
# Will include the values from index 1 to index 3, but not including index 3
print(my_list[1:3])

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)