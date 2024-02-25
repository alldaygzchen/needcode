# BFS(O(4*m*n)) 
# Find the shortest path

from collections import deque
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
# the best
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    idx=0
    length = 0
    while True:
        
        # print('level',idx)
        
        if idx==0:
            queue.append((0, 0))
            visit.add((0, 0))

        if not queue:
            return length
        
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                visit.add((r + dr, c + dc)) #important, not visiting the same position twice (not removing)
                queue.append((r + dr, c + dc))

        length += 1
        idx+=1


def dfs_traversal(grid, r, c,visit,path_length,min_path_length):

    ROWS, COLS = len(grid), len(grid[0])
    

    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return
    if r == ROWS - 1 and c == COLS - 1:
        min_path_length[0] = min(min_path_length[0], path_length)
        return

    visit.add((r, c))

    dfs_traversal(grid, r + 1, c, visit,path_length+1,min_path_length)
    dfs_traversal(grid, r - 1, c, visit,path_length+1,min_path_length)
    dfs_traversal(grid, r, c + 1, visit,path_length+1,min_path_length)
    dfs_traversal(grid, r, c - 1, visit,path_length+1,min_path_length)

    visit.remove((r, c))

def dfs_divide_conquer(grid, r, c, visit,path_length):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return float('inf')
    if r == ROWS - 1 and c == COLS - 1:
        return path_length

    visit.add((r, c))


    shortest_path = min(
        dfs_divide_conquer(grid, r + 1, c, visit,path_length)+1,
        dfs_divide_conquer(grid, r - 1, c, visit,path_length)+1,
        dfs_divide_conquer(grid, r, c + 1, visit,path_length)+1,
        dfs_divide_conquer(grid, r, c - 1, visit,path_length)+1
    )

    visit.remove((r, c))
    return shortest_path

if __name__=="__main__":
    print('bfs', bfs(grid))
    min_path_length_traversal= [float('inf')]
    dfs_traversal(grid, 0, 0,set(),0,min_path_length_traversal)
    print('dfs_traversal',min_path_length_traversal[0])
    print('dfs_divide_conquer',dfs_divide_conquer(grid, 0, 0,set(),0))