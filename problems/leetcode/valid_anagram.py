def is_anagram(s, t)  -> bool:
    if len(s) != len(t):
        return False

    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False

    return True


assert is_anagram("anagram", "nagaram") is True
assert is_anagram("rat", "car") is False
assert is_anagram("aacc", "ccac") is False
assert is_anagram("a", "aa") is False
assert is_anagram("", "") is True
print("All tests passed")