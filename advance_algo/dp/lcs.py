# Brute Force
# time complexity O(2^(m+n))
# Memoization
# time complexity
class Solution:
    # def bruteForce(self,s1,s2):
    #     self.s1 = s1
    #     self.s2 = s2
    #     return self.helper(0,0)
    
    # def helper(self,i1,i2):
        
    #     # base case
    #     if i1 == len(self.s1) or i2 == len(self.s2):
    #         return 0
        
    #     if self.s1[i1] == self.s2[i2]:
    #         return 1 + self.helper(i1+1,i2+1)
    #     else:
    #         return max(self.helper(i1+1,i2),self.helper(i1,i2+1))

    def memoization(self,s1,s2):
        """
        create a helper function where store the lcs of i1,i2 
        
        """
        self.s1 = s1
        self.s2 = s2
        self.cache = [[None]*len(s2) for _ in range(len(s1))]
        return self.helper(0,0)
    
    def helper(self,i1,i2):
        
        # base case
        if i1 == len(self.s1) or i2 == len(self.s2):
            return 0
        # cache case 
        ## does not include out of bound cases
        if self.cache[i1][i2]:
            return self.cache[i1][i2]
        
        if self.s1[i1] == self.s2[i2]:
            self.cache[i1][i2] = 1 + self.helper(i1+1,i2+1)
            return self.cache[i1][i2]
        else:
            self.cache[i1][i2] =  max(self.helper(i1+1,i2),self.helper(i1,i2+1))
            return self.cache[i1][i2]

    # def dp(self,s1,s2):
        
    #     M,N = len(s1),len(s2)
    #     cache = 
        
if __name__=="__main__":
    # s = Solution()
    # print('bruteForce',s.bruteForce("adcb","abc"))
    s = Solution()
    print('memoization',s.memoization("adcb","abc"))
    # s = Solution()

