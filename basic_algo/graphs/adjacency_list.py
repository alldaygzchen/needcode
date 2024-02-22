
from collections import deque

## Count the path

# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


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
print('adjList',adjList)


# Count paths (backtracking) O(N^vertexs) high
def dfs_divide_conquer(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs_divide_conquer(neighbor, target, adjList, visit)
    visit.remove(node)

    return count


def dfs_traversal(node, target, adjList, visit,count):
    if node in visit:
        return
    if node == target:
        count[0]+=1
        return
    
    visit.add(node)
    for neighbor in adjList[node]:
        dfs_traversal(neighbor, target, adjList, visit,count)
    visit.remove(node)


if __name__=="__main__":
    print('dfs_divide_conquer',dfs_divide_conquer("A", "E", adjList, set()))
    count = [0]
    dfs_traversal("A", "E", adjList, set(),count)
    print('dfs_traversal',count[0])