
"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target, 
where the value of each distinct candidate are unlimited.
"""

"""
explore all the solutions, we use backtracking
1. create global variables
2. create a helper function where idx is the current value and curSet
3. creating ending cases and the process to go to another helper function

"""



from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.sets = []
        self.target =target
        self.helper(0,[])
        return self.sets
    
    def helper(self,idx,cur_set):
        
        # ending case for backtracking
        if self.target == sum(cur_set):
            self.sets.append(cur_set.copy())
            return 
        if self.target< sum(cur_set):
            return 
        if idx == len(self.candidates):
            return

        # add candidates[idx] and go to another helper function
        cur_set.append(self.candidates[idx])
        self.helper(idx,cur_set)
        cur_set.pop()
        self.helper(idx+1,cur_set)

if __name__=="__main__":
    s= Solution()
    print(s.combinationSum([2,3,6,7],7)) #[[2,2,3],[7]]
    s= Solution()
    print(s.combinationSum([2,3,5],8)) #[[2,2,2,2],[2,3,3],[3,5]]
    s= Solution()
    print(s.combinationSum([2],1)) #[]