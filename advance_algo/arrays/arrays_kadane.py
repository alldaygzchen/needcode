# 53. Maximum Subarray
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curSum = 0
        maxSum = float("-inf")
        L=0
        
        for R in range(len(nums)):
            curSum=max(curSum+nums[R],nums[R])
            if curSum == nums[R]:
                L=R
            maxSum = max(maxSum,curSum)

        return maxSum



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for idx =0
        maxCurrentSum = nums[0]
        maxOverallSum = nums[0]

        for idx in range(1,len(nums)):
            maxCurrentSum = max(maxCurrentSum+nums[idx],nums[idx])
            maxOverallSum = max(maxCurrentSum,maxOverallSum)

        return maxOverallSum

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurrentSums = [float('-inf')]*len(nums)
        maxCurrentSums[0]=nums[0]

        for idx in range(1,len(nums)):
            maxCurrentSums[idx] = max(maxCurrentSums[idx-1]+nums[idx],nums[idx])

        return max(maxCurrentSums)
    
class SolutionRec1:
    def maxSubArray(self, nums: List[int]) -> int:
        self.nums = nums
        self.maxCurrent =float('-inf')
        self.maxOverall = float('-inf')
        self.myRecursion(len(nums)-1)
        return self.maxOverall 


    def myRecursion(self,idx):
        # the output is to calculate (0,idx) self.maxCurrent
        if idx==0:
            self.maxCurrent = self.nums[0]
            self.maxOverall= self.nums[0]
            return self.maxCurrent

        self.maxCurrent = max(self.nums[idx]+self.myRecursion(idx-1),self.nums[idx])
        self.maxOverall=max(self.maxCurrent,self.maxOverall)
        return self.maxCurrent
  
class SolutionRec2:
    def maxSubArray(self, nums: List[int]) -> int:
        self.nums = nums
        self.collect =[None]*len(nums)
        self.myRecursion(len(nums)-1)
        return max(self.collect)


    def myRecursion(self,idx):

        # if self.collect[idx]:
        #     print('HIHI')
        #     return self.collect[idx]

        if idx==0:
            self.collect[0] = self.nums[0]
            return self.collect[0]

        self.collect[idx] = max(self.nums[idx]+self.myRecursion(idx-1),self.nums[idx])
        return self.collect[idx]

if __name__=="__main__":
    s=SolutionRec2()
    print(s.maxSubArray([2, 3, 4, 5, 7]))