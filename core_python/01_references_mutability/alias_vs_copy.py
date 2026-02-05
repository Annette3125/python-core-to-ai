print("== Alias ==")
a = [1, 2]
b = a
b.append(99)
print("a:", a)  # Expected: [1, 2, 99]
print("b:", b)  # Expected: [1, 2, 99]

print("\n== Shallow copy (flat list) ==")
a = [1, 2]
b = a[:]        # new outer list
b.append(99)
print("a:", a)  # Expected: [1, 2]
print("b:", b)  # Expected: [1, 2, 99]