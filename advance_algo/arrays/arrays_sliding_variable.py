#209. Minimum Size Subarray Sum
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        output_length = float("inf")
        left = 0
        current_total =0
        
        for right in range(len(nums)):
            
            current_total+=nums[right]
            
            while current_total >=target:
                print(output_length,right-left+1,left,right)
                output_length = min(output_length,right-left+1)
                current_total-=nums[left]
                left+=1
        return 0 if output_length == float("inf") else output_length



class SolutionRC:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        self.target = target
        self.nums = nums
        self.current_total = 0
        self.miminum_length= float("inf")
        self.helper(0,0)
        return 0 if self.miminum_length == float("inf") else self.miminum_length
    def helper(self,L,R):
        # the output is to calculate (L,R) self.current_total

        if R>=len(self.nums):
            return 
        
        self.current_total+=self.nums[R]
        while self.current_total>=self.target:
            self.miminum_length = min(self.miminum_length,R-L+1)
            self.current_total-=self.nums[L]
            L+=1

        return self.helper(L,R+1)
    
if __name__=="__main__":
    s = SolutionRC()
    print(s.minSubArrayLen(7,[2,3,1,2,4,3]))
    print(s.minSubArrayLen(4,[1,4,4]))
    print(s.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))