
def is_anagram(s, t):
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

def clean(s) -> str:
    out = []
    for ch in s:
        if ch.isalnum():
            out.append(ch.lower())
    return "".join(out)


def is_anagram_clean(s, t) -> bool:
    s2 = clean(s)
    t2 = clean(t)
    return is_anagram(s2, t2)


assert is_anagram_clean("Dirty room!!", "Dormitory") is True
assert is_anagram_clean("abc", "abç") is False
assert is_anagram("ab", "ac") is False
print("All tests passed")