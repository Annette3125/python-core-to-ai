def first_unique_char(s: str) -> str:

    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in s:
        if counts[ch] == 1:
            return ch

    return "_"



assert first_unique_char("leetcode") == "1"
assert first_unique_char("aabbcc") == "_"
print("All tests passed")

