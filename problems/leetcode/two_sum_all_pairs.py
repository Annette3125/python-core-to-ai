def two_sum_all_pairs(nums, target):
    pairs = []
    seen = {}

    for i, x in enumerate(nums):
        need = target - x

        if need in seen:
            for j in seen[need]:
                pairs.append([j, i])

        if x not in seen:
            seen[x] = []
        seen[x].append(i)

    return pairs

print(two_sum_all_pairs([2, 7, 2, 7], 9))
#  Expected: [[0, 1], [1, 2], [0, 3], [2, 3]]
print(two_sum_all_pairs([3, 3, 3], 6))
#  Expected: [[0, 1], [0, 2], [1, 2]]

assert two_sum_all_pairs([2, 7, 2, 7], 9) == [[0, 1], [1, 2], [0, 3], [2, 3]]
assert two_sum_all_pairs([3, 3, 3], 6) == [[0, 1], [0, 2], [1, 2]]
assert two_sum_all_pairs([], 5) == []
print("All tests passed")
