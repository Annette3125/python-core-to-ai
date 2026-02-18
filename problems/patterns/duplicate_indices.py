def duplicate_indices(nums):
    seen = {}

    for i, x in enumerate(nums):
        if x not in seen:
            seen[x] = []
        seen[x].append(i)

    result = {}
    for x, idxs in seen.items():
        if len(idxs) > 1:
            result[x] = idxs

    return result

print(duplicate_indices([1,2,1,3,2]))
# Expected: {1: [0, 2], 2: [1, 4]}

assert duplicate_indices([1,2,1,3,2]) == {1: [0, 2], 2: [1, 4]}
assert duplicate_indices([1, 2, 3]) == {}
assert duplicate_indices([]) == {}

print("All tests passed")

