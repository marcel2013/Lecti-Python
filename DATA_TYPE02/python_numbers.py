"""Python Numbers
There are three numeric types in Python:"""

# int
# float
# complex

# Variables of numeric types are created when you assign a value to them:

# Example

# x = 1         # int
# y = 10.0      # float
# z = 1j        # complex

# To verify the type of any object in Python, use the type() function:

# print(type(x))
# print(type(y))
# print(type(z))

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

# x = 1
# y = 356787614
# z = 876542

# print(type(x))
# print(type(y))
# print(type(z))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# x = 1.10
# y = 1.0
# z = 43.90

# print(type(x))
# print(type(y))
# print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

# x = 35e3
# y = 12E4
# z = -85.7e589

# print(type(x))
# print(type(y))
# print(type(z))

"""Complex
Complex numbers are written with a "j" as the imaginary part:"""


"""Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:"""

# x = 1      # int
# y = 2.6    # float
# z = 1j     # complex

# convert from int to float:

# a = float(x)
# print(a)

# convert from float to int

# b = int(y)
# print(b)

# convert from int to complex

# c = complex(x)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))


"""Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:"""

"""Număr Aleator
Python nu dispune de o funcție random() pentru a genera un număr aleatoriu, dar Python are un modul încorporat numit random care poate fi utilizat pentru a genera numere aleatoare:"""

# Import the random module, and display a random number between 1 and 9:

import random
print(random.randrange(1, 10))


"""Python Random Module"""