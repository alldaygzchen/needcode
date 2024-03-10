import heapq
# get all shortest path that start with src
def shortestPath( n: int, edges, src: int):
    """
    thoughts: since it has weight, we cannot use bfs , we use dijkstra's 
    step1: create a adjacent dic e.g. adj[src]=[[weight,des],...]
    step2: create a minHeap and add the source point e.g. minHeap = [[weight1, des],...]
    step3: every time we pop from the minHeap, we save it to the shortest e.g. {"E:5} and then add new [weight1+weight2,des] from the pop to the minHeap
    
    """
    adj = {}
    min_heap = []
    shortest = {}
    shortest[src]=0

    # consider no edge between the nodes
    for i in range(n):
        adj[i] = []


    for start,end,dist in edges:
        adj[start].append([dist,end])


    for dist,end in adj[src]:
        heapq.heappush(min_heap,[dist,end])
    


    while True:

        if not min_heap:
            for i in range(n):
                if i not in shortest:
                    shortest[i] = -1
            return shortest


        w1,n1 = heapq.heappop(min_heap)

        if n1 not in shortest:
            shortest[n1]=w1
        else:
            continue

        

        for w2,n2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(min_heap,[w1+w2,n2])
            else:
                continue





if __name__=="__main__":
    edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
    print(shortestPath(5,edges,0)) #[{0:0}, {1:7}, {2:3}, {3:9}, {4:5}]