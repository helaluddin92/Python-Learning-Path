# Assigning value to variable

counter = 100  # An integer assignment
name = "John"  # A String
result = 100.0  # A Floating Point

# print(counter)
# print(name)
# print(result)

# Multiple Assignment

x = y = z = 100

# print(x)
# print(y)
# print(z)


a, b, c = 1, 2, "John"

# print(a)
# print(b)
# print(c)


# Standard Data Type

# 1. Text type:
# String

x = "Hello World"
y = "The quick brown fox, jumps over the lazy dog."

# print(x, type(x))
# print(y, type(y))

# 2. Numeric Type
# Integer
x = 20
y = 100

# print(x, type(x))
# print(y, type(y))

# Float
x = 20.0
y = 100.25

# print(x, type(x))
# print(y, type(y))

# Complex

x = 2+5j
y = 3+2j

# print(x, type(x))
# print(y, type(y))


# 3. Sequence Type
# List
x = [1, 2, 3, 4, "Hello", True]
y = list([1, 2, 3, 4, 5])
# print(x)
# print(y)

# Tuple
x = (1, 2, 3, 4, 5, 6, "Hello", False, True)
y = 1, 2, 3, 4, 5  # Without paranthesis also be tuple
z = tuple([1, 2, 3, 4, 5, 6, "John"])  # Shoul be use square bracket

# print(x)
# print(y)
# print(z)

# Range
x = range(0, 20)

# print(x)
# print(list(x)) # To get output use list function

# 4. Mapping Type

# Dictionary

x = {"name": "John", "age": 20}  # Here [key:value]
y = dict(name="John", age=20)

# print(x)
# print(y)

# 5. Set Type

# Set
x = {1, 2, 3, 4, 5, 6}
y = set([1, 2, 3, 4, 5, 6])
# print(x)
# print(y)

# Frozenset

# In frozenset we cannot change the value of set.

x.add(20)
# print(x)

x = frozenset([1, 2, 3, 4, 5, 6, 7, 8])

# x.add(9) # It can't possible to add 9 and we will get error when run.

# 6. Boolean
# True
# False

# 7. Binary Type

#bytes, bitearray, memoryview

x = bytes(5)  # bytes
x = bytearray(5)  # bytearray
x = memoryview(bytes(5))  # Memory view
