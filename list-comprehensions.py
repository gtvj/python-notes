# A list created based on another list or iterator

seq = range(11)

# List comprehension to double all items in the sequence
seq2 = [x * 2 for x in seq]
print(seq2)

# List comprehension to remove those that are not divisible by 3
seq3 = [x for x in seq if x % 3 != 0]
print(seq3)

# List of tuples (cubed in this case)
seq4 = [(x, x ** 3) for x in seq]
print(seq4)

# Dictionary from sequence
seq4 = {x: x ** 5 for x in seq}
print(seq4)

# Set from sequence
seq5 = {x for x in 'supercool' if x not in 'olp'}
print(seq5)

