# A set is an unordered collection with no duplicate elements
# Sets also include union, intersection, difference, and symmetric difference

'''
Characteristics of a Set

Unordered: Sets do not record the order of elements
Unique: Sets automatically remove duplicates, ensuring that each element is unique
Mutable: You can add or remove elements from a set
Set Type: Sets are represented with curly braces {} or set() constructor
'''

my_set = {1, 2, 3}

# To create a empty set use set(), not {} that is a empty dictionary
empty_set = set()

# Adding a element to a set
my_set.add(4)

# Removing a element from a set
my_set.remove(3)

# Discard will remove a element from the set if it exists but no error if missing
my_set.discard(5)

# Will remove a arbitrary element from the set
my_set.pop()

# Removes all elements
my_set.clear()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union() (or |): Returns a set containing all elements from both sets (removes duplicates).
# intersection() (or &): Returns a set with elements common to both sets.
# difference() (or -): Returns a set with elements in the first set but not in the second.
# symmetric_difference() (or ^): Returns a set with elements in either set but not in both.
    
print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference: {1, 2}
print(set1 ^ set2)  # Symmetric Difference: {1, 2, 4, 5}

# Set membership testing
s = {1, 2, 3}
print(2 in s)   # True
print(4 in s)   # False

# Iterating over a set
s = {1, 2, 3}
for element in s:
    print(element)

# Removing duplicates from a list using a set
my_list = [1, 2, 2, 3, 3, 4]
unique_list = list(set(my_list))  # Output: [1, 2, 3, 4]
