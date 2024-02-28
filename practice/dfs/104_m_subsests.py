"""
Given a list of distinct numbers, return all posible distinct subsets
time complexity:  O(n*2^n)
space complexity: O(n) #height of the tree
"""
"""
explore all the solutions, we use backtracking

"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.subsets = []
        self.helper(0,[])
        return self.subsets

    def helper(self,idx,current_subset):
        # ending case
        if idx == len(self.nums):
            self.subsets.append(current_subset.copy())
            return

        # purpose
        current_subset.append(self.nums[idx])
        self.helper(idx+1,current_subset)
        current_subset.pop()
        self.helper(idx+1,current_subset)


if __name__=="__main__":
    s= Solution()
    print(s.subsets([0]))
    s= Solution()
    print(s.subsets([1,2,3]))