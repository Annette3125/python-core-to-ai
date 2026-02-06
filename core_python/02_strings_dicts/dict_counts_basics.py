#  1
s="abca"
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
# Expected: {'a': 2, 'b': 1, 'c': 1}

# 2

def first_unique(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1

print(first_unique("loveleetcode"))
#  Expected: 2

# 3
arr = [1, 2, 2, 3, 3]
seen = set()
for x in arr:
    if x not in seen:
        seen.add(x)
print(seen)
#  Expected: {1, 2, 3}

# 4
print("a" in {"a": 1})   # Expected: True (dict checks keys)
print("a" in {"a", "b"}) # Expected: True (set checks elements)