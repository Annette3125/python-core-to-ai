def max_sum_subarray(nums, k):
    if k <= 0 or k > len(nums):
        return None

    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        best = max(best, window_sum)

    return best

assert max_sum_subarray([2,1,5,1,3,2], 3) == 9
assert max_sum_subarray([2,3,4,1,5], 2) == 7
print("All tests passed")
