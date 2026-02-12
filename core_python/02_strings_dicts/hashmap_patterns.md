## O(n) vs O(n²)

### O(n) means “grows linearly”
If `n` doubles, the work roughly doubles.

Examples:
- 10 numbers → ~10 checks
- 100 numbers → ~100 checks
- 1,000 numbers → ~1,000 checks

**Two Sum with a dict is O(n)** because:
- you iterate through the list once
- each lookup like `need in seen` is very fast (approximately O(1))

### O(n²) means “grows quadratically”
If `n` doubles, the work grows about 4×.

Examples:
- n = 10 → ~100 pairs
- n = 100 → ~10,000 pairs
- n = 1,000 → ~1,000,000 pairs

**Two Sum with two loops (checking all pairs i, j) is O(n²)**.

Why “quadratic”?
Because for each element (~n times), you check many other elements (~n times):
`n * n = n²`.

## Hashmap patterns

### Counting pattern
Use a dict to count how many times each item appears.
Typical use cases: anagrams, frequency counting, first unique character.

```
counts[x] = counts.get(x, 0) + 1
```


### Seen pattern
Use a set/dict to remember what you've already seen while iterating.
Typical use cases: duplicates, Two Sum, fast membership checks.

```
if x in seen: ...; seen.add(x)
```
