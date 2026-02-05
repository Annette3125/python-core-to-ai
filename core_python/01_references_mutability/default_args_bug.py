def add(v, lst=[]):
    lst.append(v)
    return lst
x = add(1)
y = add(2)
print(x, y)
# Expected: [1, 2] [1, 2]

def add(v, lst=None):
    if lst is None:
        lst = []
    lst.append(v)
    return lst

x = add(1)
y = add(2)
print(x, y)

# Expected: [1] [2]