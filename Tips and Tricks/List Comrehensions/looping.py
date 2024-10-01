fruits = ['apple', 'banana', 'cherry']
# Without index
for fruit in fruits:
    print(fruit)

# Using index
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

names = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(names):
    print(index, name)

# With index and value
names = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(names):
    print(index, name)

for i in range(3):
    print(i)
else:
    print("Loop completed!")

for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)

for i in range(5):
    if i == 3:
        continue  # Skip the current iteration when i is 3
    print(i)

for i in range(5):
    if i == 3:
        pass  # Do nothing and move to the next iteration
    print(i)

# Looping through multiple arrays
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)