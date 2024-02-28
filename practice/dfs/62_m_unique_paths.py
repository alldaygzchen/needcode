class Solution:
    # dfs memoization
    def uniquePaths(self, m: int, n: int) -> int:
        self.m =m 
        self.n =n
        self.cache = [[None]*(n) for _ in range(m)]
        return self.helper(0,0)

    def helper(self,r,c):
        
        if r==self.m-1 and c==self.n-1:
            return 1
        if r==self.m or c == self.n:
            return 0
        
        if self.cache[r][c]:
            return self.cache[r][c]
        
        return self.helper(r+1,c)+self.helper(r,c+1)

if __name__=="__main__":   
    s = Solution()
    print(s.uniquePaths(3,7))
    print(s.uniquePaths(3,2))




