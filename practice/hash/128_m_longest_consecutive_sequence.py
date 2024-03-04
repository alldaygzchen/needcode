from typing import List
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        
        # prepare
        l = 0
        r = 0
        prev = None
        nums = sorted(set(nums))
        print('nums',nums)
        max_length = 0
        

        while True:
            # print('#######')
            # print('prev:',prev,'prev_max_length',max_length)
            # print('nums[l]:',nums[l],'nums[r]:',nums[r])

            if r == len(nums):
                return max_length
            
            if prev is not None  and prev+1!=nums[r]:
                # max_length = max(r-1-l+1,max_length)
                prev = nums[r]
                l=r
                r+=1
                continue
            max_length = max(r-l+1,max_length)
            prev = nums[r]
            r+=1
            
    
if __name__=="__main__":
    nums =[[4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3],[9,1,4,7,3,-1,0,5,8,-1,6],[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1]]
    # nums =[[9,1,4,7,3,-1,0,5,8,-1,6]]
    for num in nums:
        sol =Solution()
        print('output',sol.longestConsecutive(num))
