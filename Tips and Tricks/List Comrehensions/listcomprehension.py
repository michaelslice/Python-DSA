# List comprehensions provide a a consise way to create lists 
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# Can be simplified to 
squares = list(map(lambda x: x**2, range(10)))