def longest_unique_substring_v2(s: str) -> int:
    left = 0
    best = 0
    last = {}  # char -> last index where it appeared

    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1

        best = max(best, right - left + 1)
        last[ch] = right

    return best


def longest_unique_substring_v1(s: str) -> int:

    left = 0
    best = 0
    seen = set()

    for right in range(len(s)):
        ch = s[right]

        while ch in seen:
            seen.remove(s[left])
            left += 1

        seen.add(ch)
        best = max(best, right - left + 1)

    return best


tests = [
    ("", 0),
    ("a", 1),
    ("abca", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("abba", 2),
]

for s, expected in tests:
    assert longest_unique_substring_v1(s) == expected
    assert longest_unique_substring_v2(s) == expected
    assert longest_unique_substring_v1(s) == longest_unique_substring_v2(s)

print("All tests passed")