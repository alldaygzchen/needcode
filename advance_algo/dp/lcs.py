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

    # def memoization(self,s1,s2):
    #     """
    #     create a helper function where store the lcs of i1,i2 
        
    #     """
    #     self.s1 = s1
    #     self.s2 = s2
    #     self.cache = [[None]*len(s2) for _ in range(len(s1))]
    #     return self.helper(0,0)
    
    # def helper(self,i1,i2):
        
    #     # base case
    #     if i1 == len(self.s1) or i2 == len(self.s2):
    #         return 0
    #     # cache case 
    #     ## does not include out of bound cases
    #     if self.cache[i1][i2]:
    #         return self.cache[i1][i2]
        
    #     if self.s1[i1] == self.s2[i2]:
    #         self.cache[i1][i2] = 1 + self.helper(i1+1,i2+1)
    #         return self.cache[i1][i2]
    #     else:
    #         self.cache[i1][i2] =  max(self.helper(i1+1,i2),self.helper(i1,i2+1))
    #         return self.cache[i1][i2]

    # def dp(self, text1: str, text2: str) -> int:
    #     M,N = len(text1),len(text2)
    #     cache = [[0]*N for _ in range(M)]
    #     duplicate_col =False
    #     duplicate_row =False

    #     if text1[0]==text2[0]:
    #         cache[0][0]=1
    #         duplicate_col =True
    #         duplicate_row=True

    #     for col in range(1,N):
    #         if text1[0]==text2[col] and not duplicate_col:
    #             cache[0][col]=1+cache[0][col-1]
    #             duplicate_col =True
    #         else:
    #             cache[0][col]=cache[0][col-1]
        
        
    #     for row in range(1,M):
    #         if text2[0]==text1[row] and not duplicate_row:
    #             cache[row][0]=1+cache[row-1][0]
    #             duplicate_row =True
    #         else:
    #             cache[row][0]=cache[row-1][0]

    #     for row in range(1,M):
    #         for col in range(1,N):
    #             if text1[row] ==text2[col]:
    #                 cache[row][col] = 1+ cache[row-1][col-1]
    #             else:
    #                 cache[row][col] = max(cache[row-1][col],cache[row][col-1])

    #     return cache[-1][-1]        

    # def dp(self, text1: str, text2: str) -> int:
    #     M,N = len(text1),len(text2)
    #     cache = [[0]*(N+1) for _ in range(M+1)]

    #     for row in range(1,M+1):
    #         for col in range(1,N+1):
    #             if text1[row-1] ==text2[col-1]:
    #                 cache[row][col] = 1+ cache[row-1][col-1]
    #             else:
    #                 cache[row][col] = max(cache[row][col-1],cache[row-1][col])

    #     return cache[-1][-1]  


    def dp(self, text1: str, text2: str) -> int:
        M,N = len(text1),len(text2)
        cache = [0]*(N+1)

        for row in range(1,M+1):
            cur_row = [0]*(N+1)
            for col in range(1,N+1):
                if text1[row-1] ==text2[col-1]:
                    cur_row[col] = 1+ cache [col-1]
                else:
                    cur_row[col] = max(cur_row[col-1],cache[col])
            cache = cur_row
            print('cache',cache)
        return cache[-1]             

        
if __name__=="__main__":
    # s = Solution()
    # print('bruteForce',s.bruteForce("adcb","abc"))
    # s = Solution()
    # print('memoization',s.memoization("adcb","abc"))
    s = Solution()
    print("dynamic programming",s.dp("adcb","abc"))

