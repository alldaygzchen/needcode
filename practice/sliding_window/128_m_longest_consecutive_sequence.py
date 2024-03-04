from typing import List
"""
1. prev = 0 => bool:false
2. set is not sorted
3. set cannot use pointer (for loop)

"""
# class Solution:

#     def longestConsecutive(self, nums: List[int]) -> int:
        
#         # prepare
#         nums = set(nums)
#         max_length = 0
#         curr_length = 0

#         for num in nums:

#             if num-1 in nums:
#                 continue

#             curr_length = 0

#             while num in nums:
#                 num+=1
#                 curr_length +=1
#                 max_length = max(curr_length,max_length)

#         return max_length
        
# class Solution:

#     def longestConsecutive(self, nums: List[int]) -> int:
        
#         # prepare
#         l = 0
#         r = 0
#         prev = None
#         nums = sorted(set(nums))
#         # print('nums',nums)
#         max_length = 0
        

#         while True:
#             if r == len(nums):
#                 return max_length
            
#             if prev is not None  and prev+1!=nums[r]:
#                 prev = nums[r]
#                 l=r
#                 r+=1
#                 continue
#             max_length = max(r-l+1,max_length)
#             prev = nums[r]
#             r+=1
    
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        
        # prepare
        l = 0
        r = 1
        prev = nums[l]
        nums = sorted(set(nums))
        # print('nums',nums)
        max_length = 0
        

        while True:
            if r == len(nums):
                return max_length
            
            if prev+1!=nums[r]:
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
