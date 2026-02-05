## Mini cheat-sheet

- `==` checks value equality; `is` checks identity (same object).

- `a + b` creates a new list; `a += b` usually mutates the list in place.

- Shallow copy (`a[:]`, `a.copy()`) copies the outer container; nested objects are shared.

- Deep copy (`copy.deepcopy`) copies nested objects too.

- Avoid mutable default arguments: use `None` and create the list inside the function.

- Matrix aliasing pitfall: `[[0] * m] * n` reuses the same row reference.



