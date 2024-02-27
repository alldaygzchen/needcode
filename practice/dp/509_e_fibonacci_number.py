class Solution:
    def fib(self, n: int) -> int:
            cache = [0,1]
            i=2


            while True:

                if n <=1:
                    return cache[n]

                if i==n+1:
                    return cache[1]


                tmp = cache[0]
                cache[0] =cache[1]
                cache[1]=tmp+cache[1]
                i+=1

if __name__=="__main__":
     s= Solution()
     print(s.fib(4)) #3