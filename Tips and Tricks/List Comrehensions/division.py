import math

# Divison is decimal by default
print(5 / 2)

# Double slash rounds down
print(5 // 2)

# A workaround for rounding towards zero is to use decimal division
# then convert to int
print(int(-3 / 2))

# More math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))