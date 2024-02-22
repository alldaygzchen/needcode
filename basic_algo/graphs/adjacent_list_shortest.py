from collections import deque
# BFS(O(V))
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