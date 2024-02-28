"""
Given a list of nums with all distinct elements, return all possible distinct permutations
"""
"""
explore all the solutions, we use backtracking
1. create global variables
2. create a helper function where idx is the current value and curSet
3. creating ending cases and the process to go to another helper function
"""


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums =nums
        self.sets = []
        self.helper([])
        return self.sets
    def helper(self,cur_set):

        """
            add the current val to the current_set and define next_val
        """
        
        if len(cur_set) == len(self.nums):
            self.sets.append(cur_set.copy())
            return 
        
        for i in range(len(self.nums)):
            if self.nums[i] in cur_set:
                continue
            cur_set.append(self.nums[i])
            self.helper(cur_set)
            cur_set.pop()





class SolutionDC:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums =nums
        return self.helper(0)
    def helper(self,idx):

        """
            add the current val to the previous result
        """

        # base case
        if idx == len(self.nums):
            return [[]]
        
        prev_perms = self.helper(idx+1)
        current_perms=[]
        for prev_perm in prev_perms:
            for j in range(len(prev_perm)+1):
                copy_perm = prev_perm.copy()
                copy_perm.insert(j,self.nums[idx])
                current_perms.append(copy_perm)
        return current_perms


if __name__=="__main__":

    s= Solution()
    print(s.permute([1,2,3])) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    s= Solution()
    print(s.permute([0,1])) #[[0,1],[1,0]]    
    s= Solution()
    print(s.permute([1])) #[[1]]


################################################################################################

    # s= SolutionDC()
    # print(s.permute([1,2,3])) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    # s= SolutionDC()
    # print(s.permute([0,1])) #[[0,1],[1,0]]    
    # s= SolutionDC()
    # print(s.permute([1])) #[[1]]