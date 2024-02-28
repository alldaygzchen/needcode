"""
Given a list of nums with elements (not all distinxr), return all possible permutations
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
        self.sets = []
        # self.visited = {}
        self.helper([])
        return self.sets
    def helper(self,cur_set):

        print('cur_set',cur_set)

        """
            add the current val to the current_set and define next_val
        """
        
        # base case
        if len(cur_set) == len(self.nums):
            self.sets.append(cur_set.copy())
            return
        
        for i in range(len(self.nums)):
            # print('start',i)

            if self.nums[i] not in cur_set:
                
                while i+1!= len(self.nums) and self.nums[i]==self.nums[i+1]:
                    # print('i',i)
                    i+=1


                cur_set.append(self.nums[i+1])
                self.helper(cur_set)
                cur_set.pop()


if __name__=="__main__":

    s= Solution()
    print(s.permuteUnique([1,1,2])) #[[1,1,2],[1,2,1],[2,1,1]]
    s= Solution()
    print(s.permuteUnique([1,2,3])) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 

