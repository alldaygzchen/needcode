
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0
        curr_sum =0
        overall_min = float('inf')

        while True:

            if r==len(nums):
                if overall_min == float('inf'):
                    return 0
                return overall_min

            curr_sum+=nums[r]
            
            while  curr_sum >= target:
                overall_min = min (overall_min,r-l+1)
                curr_sum-=nums[l]
                l+=1
            
            r+=1
            
            






if __name__=="__main__":
    s = Solution()
    print(s.minSubArrayLen(7,[2,3,1,2,4,3])) #2
    print(s.minSubArrayLen(4,[1,4,4])) #1
    print(s.minSubArrayLen(11,[1,1,1,1,1,1,1,1])) #0