from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        idx=1
        cache = [None]*len(nums)

        if nums[0] == 0:
            cache[0] =(1,1)
        else:
            cache[0] = (nums[0],nums[0])

        res = max(nums)

        while True:

            if idx==len(nums):
                return res
            
            prev_min,prev_max = cache[idx-1]
            curr_min = min(prev_min*nums[idx],prev_max*nums[idx],nums[idx])
            curr_max = max(prev_min*nums[idx],prev_max*nums[idx],nums[idx])
            cache[idx] = (curr_min,curr_max)
            res = max(res,curr_max)
            idx+=1
        
        



if __name__ =="__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))
        