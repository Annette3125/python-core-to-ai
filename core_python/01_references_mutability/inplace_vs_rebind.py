#   1
a = [1,2]
b = a
b += [3]
print(a, b)
# Expected: [1,2, 3] [1,2, 3]

#  2
a = [1,2]
b = a
b = b + [3]
print(a, b)
# Expected: [1, 2] [1, 2, 3]
print(a is b)  # Expected: True (first), False (second after rebinding)
