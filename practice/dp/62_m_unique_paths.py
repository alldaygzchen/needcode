class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.m =m 
        self.n =n
        self.cache = [1]*(n)
        r = m-2
        
        while True:

            if r==-1:
                return self.cache[0]
            curRow = [None]*n
            curRow[-1]=1
            for c in range(n-2,-1,-1):
                curRow[c] = self.cache[c]+curRow[c+1]

            self.cache = curRow
            r-=1


if __name__=="__main__":   
    s = Solution()
    print(s.uniquePaths(3,7))
    print(s.uniquePaths(3,2))




