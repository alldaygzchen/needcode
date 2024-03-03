from typing import List
class Solution:

    def __init__(self):
        self.parent = None
        self.rank = None

    def find(self,e):

        while True:
            if e == self.parent[e]:
                return e
        
            self.parent[e] =self.parent[self.parent[e]]
            e= self.parent[e]
            
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
            self.parent[p2] = p1
            self.rank[p2]+=1

        return True
        


    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)

        self.parent = {num: num for num in nums}
        self.rank = {num: 0 for num in nums}

 

        for num in nums:
            if num+1 in self.parent:
                self.union(num,num+1)
            # if num-1 in self.parent:
            #     self.union(num-1,num)



        root_count = {}
        for root in self.parent.values():
            root_count[root] = root_count.get(root,0)+1


        return max(root_count.values())
    
if __name__=="__main__":
    nums =[[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    for num in nums:
        sol =Solution()
        print('output',sol.longestConsecutive(num))
