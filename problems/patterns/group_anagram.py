def group_anagrams(words):

    groups = {}

    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


out = group_anagrams(["eat","tea","tan","ate","nat","bat"])

assert sorted([sorted(g) for g in out]) == sorted([["ate","eat","tea"],["nat","tan"],["bat"]])

print("All tests passed")
