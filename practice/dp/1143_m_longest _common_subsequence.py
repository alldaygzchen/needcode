class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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
        return cache[-1]       
    
if __name__=="__main__":

    s = Solution()
    print("longestCommonSubsequence",s.longestCommonSubsequence("adcb","abc"))
