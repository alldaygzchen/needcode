grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Count paths (backtracking)(divide and conquer)
def dfs_divide_conquer(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs_divide_conquer(grid, r + 1, c, visit)
    count += dfs_divide_conquer(grid, r - 1, c, visit)
    count += dfs_divide_conquer(grid, r, c + 1, visit)
    count += dfs_divide_conquer(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count


def dfs_traversal(grid, r, c, visit,count):

    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return
    if r == ROWS - 1 and c == COLS - 1:
        count[0]+=1
        return

    visit.add((r, c))

    dfs_traversal(grid, r + 1, c, visit,count)
    dfs_traversal(grid, r - 1, c, visit,count)
    dfs_traversal(grid, r, c + 1, visit,count)
    dfs_traversal(grid, r, c - 1, visit,count)

    visit.remove((r, c))

if __name__=="__main__":
    print(dfs_divide_conquer(grid, 0, 0, set())) #2
    count = [0]
    dfs_traversal(grid, 0, 0, set(),count)
    print(count[0]) #2