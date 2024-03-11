from typing import List
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        # create adj
        adj ={} 
        for i in range(n):
            adj[i]=[]

        # fill in the adj
        for src,des,dis in edges:
            adj[src].append([dis,des])
            adj[des].append([dis,src])

        # create a min heap
        min_heap = []

        for dis,des in adj[0]:
            heapq.heappush(min_heap,[dis,0,des])

        # create a visited set
        visited = set()
        visited.add(0)

        # minimum spanning tree
        mst = []
        total_dis = 0

        while True:

            if not min_heap:
                return (mst,total_dis) if len(visited) == n else (-1,-1) 
            
            dis,src,node= heapq.heappop(min_heap)

            if node in visited:
                continue

            mst.append([src,node])
            visited.add(node)
            total_dis+=dis

            for dis,des in adj[node]:
                if des not in visited:
                    heapq.heappush(min_heap,[dis,node,des])



if __name__ =="__main__":
    s = Solution()
    mst,total_dis= s.minimumSpanningTree(5,[[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]])
    print(mst,total_dis)