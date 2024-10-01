# Dictionary is a data structure of a set of key-value pairs, where 
# each key is unique and used to access its associated value

# Basic Characteristics of Dictionaries
# Key-value pairs: Each element in a dictionary consists of a key and a value
# Keys are unique, but values can be duplicated

my_dict = {"name": "Alice", "city": "Chicago"}

# Accessing Dictionary Values
# You can access a value in a dictionary by using its key in square brackets
# If the key does not exist it raises a keyError
# Using .get() method safely retrieves a value

print(my_dict["name"])
print(my_dict.get("city"))

# Adding key-value pairs to a dictionary
my_dict["Age"] = 30

# Removing key-value pairs

# Removes the key-value pair with the specified key and returns the value
my_dict.pop("city")

# Removes and returns the last inserted key-value pair insertion order is preserved
my_dict.popitem()

# Deletes the key-value pair associated with key
del my_dict["name"]

# Removes all elements from the dictionary
my_dict.clear()

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# keys(): Returns a view object with all the dictionary’s keys.
print(my_dict.keys())    # dict_keys(['name', 'age', 'city'])

# values(): Returns a view object with all the dictionary’s values.
print(my_dict.values())  # dict_values(['Alice', 30, 'New York'])

# items(): Returns a view object with all the dictionary’s key-value pairs as tuples.
print(my_dict.items())   # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Iterating over a dictionary

# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking for keys in dictionaries
# You can use the in keyword to check if a key exists in a dictionary.

if "name" in my_dict:
    print("Key exists!")

# Using tuples as dictionary keys
my_dict = {(1, 2): "Point A", (3, 4): "Point B"}
print(my_dict[(1, 2)])  # Output: Point A

# Dictionary from zip
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

my_dict = dict(zip(keys, values))
print(my_dict)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

