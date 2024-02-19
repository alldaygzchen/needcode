#219. Contains Duplicate II
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window =set()
        left=0
        
        for right in range(len(nums)):

            if nums[right] in window:
                return True 
            
            window.add(nums[right])
            
            if right-left>=k:
                window.remove(nums[left])
                left+=1
        
        return False

class SolutionRec1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        self.set=set()
        self.nums =nums
        self.k =k
        return self.helper(0,0)

    def helper(self,L,R):
         # the output is to calculate (L,R) containing self.set duplicate

        print('R',R,'self.set',self.set)

        if R==len(self.nums):
            return False
        
        if self.nums[R] in self.set:
            return True
        
        self.set.add(self.nums[R])

        if R-L>=self.k:
            self.set.remove(self.nums[L])
            L+=1
        
        return self.helper(L,R+1)
"""
idx 0 self.set set()
idx 1 self.set {1}
idx 2 self.set {1, 2}
idx-self.k 0
idx 3 self.set {2, 3}
idx-self.k 1
idx 4 self.set {1, 3}
idx-self.k 2
idx 5 self.set {1, 2}
idx-self.k 3
idx 6 self.set {2, 3}
"""
# class Solution2:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         window =set()
#         left=0
        
#         for right in range(len(nums)):

#             if right-left>k:
#                 window.remove(nums[left])
#                 left+=1

#             if nums[right] in window:
#                 return True 
            
#             window.add(nums[right])
        
#         return False

# class SolutionRec2:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
#         self.set=set()
#         self.nums =nums
#         self.k =k
#         return self.helper(0)

#     def helper(self,idx):

#         print('idx',idx,'self.set',self.set)
#         if len(self.set)>self.k:
#             self.set.remove(self.nums[idx-self.k-1])

#         if idx==len(self.nums):
#             return False

#         if self.nums[idx] in self.set:
#             return True
        
#         # print('self.set2',self.set)
#         self.set.add(self.nums[idx])
        


#         return self.helper(idx+1)

# """

# idx 0 self.set set()
# idx 1 self.set {1}
# idx 2 self.set {1, 2}
# idx 3 self.set {1, 2, 3}
# idx-self.k-1 0
# idx 4 self.set {1, 2, 3}
# idx-self.k-1 1
# idx 5 self.set {1, 2, 3}
# idx-self.k-1 2
# idx 6 self.set {1, 2, 3}
# idx-self.k-1 3

# """



# class SolutionRec3:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
#         self.set=set()
#         self.nums =nums
#         self.k =k
#         return self.helper(len(nums)-1)

#     def helper(self,idx):
#         # the output is bool

#         print('idx',idx)

#         if idx<0:
#             return False
        
#         if self.nums[idx] in self.set:
#             return True
        
#         self.set.add(self.nums[idx])

#         if len(self.set)>self.k:
#             self.set.remove(self.nums[idx+self.k])
        
#         return self.helper(idx-1)
    




