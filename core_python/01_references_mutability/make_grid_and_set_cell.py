def make_grid_loop(n, m, value=0):
    grid = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(value)
        grid.append(row)
    return grid

def make_grid_comp(n, m, value=0):
    return [[value for _ in range(m)] for _ in range(n)]

def set_cell(grid, r, c, v):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return False
    grid[r][c] = v
    return True

g = make_grid_loop(3, 2, 0)
ok = set_cell(g, 0, 0, 9)
print(ok, g)  # Expected: True [[9, 0], [0, 0], [0, 0]]

g2 = make_grid_comp(3, 2, 0)
set_cell(g2, 0, 0, 9)
print(g2)     # Expected: [[9, 0], [0, 0], [0, 0]]


"""
Note: if grid empty ([]),
then grid[0] would be a error.
now make_grid exist, creates not empty lines, that is OK.
"""



