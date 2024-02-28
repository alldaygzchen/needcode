"""
Given two nums n and k , return all possible combinations of size=k, choosing values between 1 to n
time complexity:  O(k*C(k,n))
space complexity: O(k*C(k,n)) #height of the tree
"""


"""
explore all the solutions, we use backtracking

"""

from typing import List

class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n =n
        self.k= k
        self.sets = []
        self.helper(1,[])
        return self.sets
    def helper(self,val,current_set):
        
        """
        add the val to the current_set and define next_val
        
        """

        # ending case

        if len(current_set)==self.k:
            self.sets.append(current_set.copy())
            return 
        
        if val == self.n+1:
            return 
        
        # purpose
        for i in range(val,self.n+1):
            current_set.append(i)
            self.helper(i+1,current_set)
            current_set.pop()

        



# class Solution1:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         self.n =n
#         self.k= k
#         self.sets = []
#         self.helper(1,[])
#         return self.sets
#     def helper(self,val,current_set):
        
#         """
#         to add the val to the current_set and define next_val
        
#         """

#         # ending case

#         if len(current_set)==self.k:
#             self.sets.append(current_set.copy())
#             return 
        
#         if val == self.n+1:
#             return 
        
#         # purpose
#         current_set.append(val)
#         self.helper(val+1,current_set)
#         current_set.pop()

#         self.helper(val+1,current_set)





if __name__=="__main__":
    # s= Solution1()
    # print(s.combine(4,2)) #[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    # s= Solution1()
    # print(s.combine(1,1)) #[[1]]


    s= Solution2()
    print(s.combine(4,2)) #[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    s= Solution2()
    print(s.combine(1,1)) #[[1]]