from collections import deque
# BFS(O(V+E))
# key point if neighbor not in visit: (to be checked)
def bfs(node,target,adjList):
    visit = set()
    queue = deque()
    idx=0
    length = 0
    while True:
        
        # print('level',idx)
        
        if idx==0:
            queue.append(node)
            visit.add(node)

        if not queue:
            return length
        
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length

            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)

        length += 1
        idx+=1

def dfs_traversal(node,target,adjList,visit,path_length,min_length):

    if node in visit:
        return
    if node == target:
        min_length[0] = min(min_length[0],path_length)
        return 
    visit.add(node)
    for neighbor in adjList[node]:
        dfs_traversal(neighbor,target,adjList,visit,path_length+1,min_length)
    visit.remove(node)

# no min_length
def dfs_divide_conquer(node,target,adjList,visit,path_length):
    
    if node in visit:
        return float('inf')
    
    if node == target:
        return path_length
    

    visit.add(node)
    curr_min = float('inf')
    for neighbor in adjList[node]:
        curr_min  = min(dfs_divide_conquer(neighbor,target,adjList,visit,path_length,)+1,curr_min)
    
    visit.remove(node)
    
    return curr_min







if __name__=="__main__":

    # Or use a HashMap
    adjList = { "A": [], "B": [] }


    # Given directed edges, build an adjacency list
    edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]


    adjList = {}
    for src, dst in edges:
        if src not in adjList:
            adjList[src] = []
        if dst not in adjList:
            adjList[dst] = []
        adjList[src].append(dst)


    print('bfs',bfs("A","E",adjList))
    min_length = [float('inf')]
    dfs_traversal("A","E",adjList,set(),0,min_length)
    print('dfs_traversal',min_length[0])
    min_length = [float('inf')]
    print('dfs_divide_conquer',dfs_divide_conquer("A","E",adjList,set(),0))