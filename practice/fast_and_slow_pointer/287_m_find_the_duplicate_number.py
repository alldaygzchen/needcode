from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # consider nums element as index
        # start from index zero
        slow = 0
        fast = 0 
        idx = 0 


        # there must be a cycle, get slow and fast pointer
        while True:

            if slow == fast and idx!=0:
                break

            slow = nums[slow]
            fast = nums[nums[fast]]
            idx+=1

        # get cycle start 
        slow2 = 0
        idx = 0 
        while True:

            if slow == slow2 and idx!=0:
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]
            idx+=1

if __name__=="__main__":
    s= Solution()
    print(s.findDuplicate([1,3,4,2,2]))
    print(s.findDuplicate([3,1,3,4,2]))