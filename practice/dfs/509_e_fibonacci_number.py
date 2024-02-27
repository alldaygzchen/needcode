class Solution:
    def fib(self, n: int) -> int:
        self.n = n
        self.cache = [None]*(n+1)
        return self.helper(n)
    def helper(self,n):


        # base case
        if n in (0,1):
            return n
        if self.cache[n]:
            return self.cache[n]
        
        self.cache[n] = self.helper(n-2) +self.helper(n-1)
        return self.cache[n]
        


if __name__=="__main__":
     s= Solution()
     print(s.fib(4)) #3