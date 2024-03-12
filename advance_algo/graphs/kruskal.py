import heapq 

class UnionFind:

    def __init__(self,n):
        self.par = {}
        self.rank = {}

        for i in range(1,n+1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self,n):
        
        while True:

            if self.par[n] == n:
                return n
            
            self.par[n]=self.par[self.par[n]]
            n = self.par[n]

    def union(self,n1,n2):

        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1==p2:
            return False
        
        if self.rank[p1]>self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1]<self.rank[p2]:
            self.par[p1] =p2
        else:
            self.par[p1] =p2
            self.rank[p2]+=1
        return True
            

def minimumSpanningTree(edges, n):

    """
    thoughts:

    step1: push edges in minHeap
    step2: create a unionFind instance
    step3:
        while True:
            if not minHeap:
                return mst    
            pop from the minHeap
            if u and v are connected:
                continue
            else:
                append to mst
                
    """


    min_heap = []
    mst = []
    
    for n1,n2,weight in edges:
        heapq.heappush(min_heap,[weight,n1,n2])

    unionfind = UnionFind(n)
    cost = 0

    while True:
        if not min_heap:
            if len(mst)==n-1:
                return mst,cost
            return -1,-1
        weight,n1,n2 = heapq.heappop(min_heap)
        if not unionfind.union(n1,n2):
            continue
        mst.append([n1,n2])
        cost+=weight


if __name__ =="__main__":
    edges = [[1,2,10],[2,3,4],[1,3,8],[2,4,4],[3,5,4],[3,4,4],[4,5,3]]
    print(minimumSpanningTree(edges, 5))

