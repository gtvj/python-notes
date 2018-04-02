k = """
Multi-line string
"""

# First class object
print(k.swapcase())


# And you can sub-class strings
class MyString(str):
    def __str__(self):
        return self[::-1]


l = MyString('Hello')

print(l)

# Acts on first letter of string
print('gwyn jones'.capitalize())

# Acts on first letter of every word
print('gwyn jones'.title())

# Are immutable
s1 = 'Gwyn Jones'
s2 = s1.title()

print(f'{id(s1)} is not {id(s2)} because strings are immutable')

# String formatting (aka interpolation)
x = 42
y = 73
print('the number is {} {}'.format(x, y))  # simple
print('the number is {xx} {yy}'.format(xx=x, yy=y))  # Named
print('the number is {0} {1} {0}'.format(x, y))  # Ordered
print('the number is {0:<5} {1:>5}'.format(x, y))  # Formatting instructions

z = 42 * 856
print('the number is {:,}'.format(z))  # Format number with zeros
print('the number is {:.3f}'.format(z))  # Format decimal places

# And you can use all of these with f strings
print(f'the number is {z:.3f}')

