class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}
        idx = 1

        while True:

            if idx==n+1:
                break
            self.parent[idx] =idx
            self.rank[idx] =0 
            idx+=1

    def find(self,e):
        # find the ancestor
        while True:
            if e == self.parent[e]:
                return e        

            # path compressing (optional)
            self.parent[e] = self.parent[self.parent[e]]
            e = self.parent[e]

    def union(self,e1,e2):
        
        p1 = self.find(e1)
        p2 = self.find(e2)

        if p1 == p2:
            # both have a path to the parent, thus union will fail
            return False
        elif self.rank[p1]>self.rank[p2]:
            self.parent[p2] = p1
        elif  self.rank[p1]<self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p1]+=1

        return True
    
if __name__=="__main__":
    edges = [[1,2],[4,1],[2,4]]
    disjoinsets = UnionFind(4)
    for edge in edges:
        disjoinsets.union(edge[0],edge[1])
    print(disjoinsets.parent)

    

