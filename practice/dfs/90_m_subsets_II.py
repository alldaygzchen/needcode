"""
Given a list of numbers that are not necessarilly distinct, return all posible subsets
time complexity:  O(n*2^n)
space complexity: O(n) #height of the tree
"""
"""
explore all the solutions, we use backtracking

"""
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.sets = []
        self.helper(0,[])
        return self.sets
    def helper(self,idx,current_subset):
        """
        the purpose of each helper is to add number to the current current_subset
        branches: include the next idx value and do not include any more next idx value 
        
        """
      
        # ending case
        # all idx has already been runned
        if idx == len(self.nums):
            self.sets.append(current_subset.copy())
            return

        # purpose
        current_subset.append(self.nums[idx])
        self.helper(idx+1,current_subset)
        current_subset.pop()

        while True:

            # print('idx',idx)

            # ending case
            if idx==len(self.nums)-1 or  self.nums[idx] != self.nums[idx+1]:
                #this is the next step
                self.helper(idx+1,current_subset)
                break
            # swap idx
            idx+=1
            



if __name__=="__main__":
    s= Solution()
    print(s.subsetsWithDup([1,2,2]))
    s= Solution()
    print(s.subsetsWithDup([0]))