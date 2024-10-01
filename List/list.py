
my_list = [1, 2, 3]

# Adding elements
my_list.append(4)
print(my_list)

# Printing the length of array
print("My list is size", len(my_list))

# Appending two lists together
my_other_list = [5, 6, 7]
my_list.extend(my_other_list)
print(my_list)

# Adding a element at a specfic index
# Insert 8 at index 7
my_list.insert(7, 8)
print(my_list)

# Removing a specific element from the list
my_list.remove(8)
print(my_list)

# Removing a item at a specific positon, if 
# no index is specified pop() removes and returns 
# the last item in the list
my_list.pop(0) # Popping index 0
my_list.pop()
print(my_list)

# Clearing the list
my_list.clear()
print(my_list)

# Returning the index of a specific element we search for
my_list = [1, 2, 3]
print(my_list)
print("Index of 1 is", my_list.index(1))

# Counting the appearence of a element
my_list.append(3)
print("3 appears", my_list.count(3), "times")

# Sorting a list
my_list.sort()

# Reversing a list
my_list.reverse()

# Returning a shallow copy of a list
my_list.copy()

# Deleting a element by its index instead of value
del my_list[0]
print(my_list)