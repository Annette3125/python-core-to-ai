Group-by pattern (dictionary of lists)
	•	groups[key] -> list of items
	•	if key not in groups: groups[key] = []
	•	groups[key].append(item)
	•	groups.setdefault(key, []).append(item) (short form)

Stable keys examples
	•	anagrams: key = "".join(sorted(word))
	•	duplicates/indices: key = value

Filtering
	•	keep only groups where len(list) > 1 (duplicates)
