def contains_duplicate(nums) -> bool:

    seen = set()

    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


assert contains_duplicate([1,2,3,1]) is True
assert contains_duplicate([1,2,3,4]) is False
assert contains_duplicate([]) is False

print("All tests passed")