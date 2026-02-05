import copy

print("== Shallow vs Deep (nested objects) ==")
a = [{"labels": ["A"]}, {"labels": ["B"]}]
b = a[:]                 # shallow copy (new outer list)
c = copy.deepcopy(a)     # deep copy (new outer + new nested)

b[0]["labels"].append("X")
c[1]["labels"].append("Y")

print("a:", a)  # Expected: [{'labels': ['A', 'X']}, {'labels': ['B']}]
print("b:", b)  # Expected: [{'labels': ['A', 'X']}, {'labels': ['B']}]
print("c:", c)  # Expected: [{'labels': ['A']}, {'labels': ['B', 'Y']}]

print("\n== Deep copy independent edit ==")
a = [{"labels": ["A"]}, {"labels": ["B"]}]
b = copy.deepcopy(a)
b[0]["labels"].append("X")

print("a:", a)  # Expected: [{'labels': ['A']}, {'labels': ['B']}]
print("b:", b)  # Expected: [{'labels': ['A', 'X']}, {'labels': ['B']}]