"""
Given a list of nums with elements (not all distinct), return all possible permutations
"""
"""
explore all the solutions, we use backtracking
1. create global variables
2. create a helper function where idx is the current value and curSet
3. creating ending cases and the process to go to another helper function
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.visited = [False] * len(nums)
        self.sets = []
        self.helper([])
        return self.sets
    def helper(self,cur_set):
        # print('cur_set',cur_set)

        """
            add the current val to the current_set and define next_val
        """
        
        # base case
        if len(cur_set) == len(self.nums):
            self.sets.append(cur_set.copy())
            return

        for i in range(len(self.nums)):
            if self.visited[i] or (i > 0 and self.nums[i] == self.nums[i - 1] and not self.visited[i - 1]):
                continue
            self.visited[i] = True
            cur_set.append(self.nums[i])
            self.helper(cur_set)
            cur_set.pop()
            self.visited[i] = False



if __name__=="__main__":

    s= Solution()
    print(s.permuteUnique([1,1,2])) #[[1,1,2],[1,2,1],[2,1,1]]
    s= Solution()
    print(s.permuteUnique([1,2,3])) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 

