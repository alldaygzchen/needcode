#238. Product of Array Except Self
from typing import List

# class Solution:
#     def productExceptSelf(self, nums):

#         res = [1 for _ in nums]
#         accu_left_mul =1
#         accu_right_mul =1 

#         for idx in range(len(nums)):
#             res[idx]= accu_left_mul
#             accu_left_mul*=nums[idx]


#         for idx in range(len(nums)-1,-1,-1):
#             res[idx]*= accu_right_mul
#             accu_right_mul*=nums[idx]

#         return res
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         for i in range(len(nums)-1):
#             res[i+1] = res[i] * nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res