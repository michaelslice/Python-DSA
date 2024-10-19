''' 
sequence[start:stop:step]

start: The index where the slice starts (inclusive). 
       If omitted, it defaults to the beginning of the sequence (index 0).
stop: The index where the slice ends (exclusive). 
      If omitted, it defaults to the end of the sequence.
step: The increment between each index. 
      If omitted, it defaults to 1. 
      You can use negative values to slice from the end or reverse the sequence.
'''

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

# Reversing a list
my_list = my_list[::-1]
print(my_list)