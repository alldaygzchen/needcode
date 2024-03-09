

# Brute Force O(2^n)
def fibonacci_dfs_divide_conquer(n):
    if n<=1:
        return n
    return fibonacci_dfs_divide_conquer(n-1) +fibonacci_dfs_divide_conquer(n-2)

# Since it is divide and conquer) O(2n)
def fibonacci_memoization(n,cache):
    
    if n<=1:
        return n
    if n in cache:
        return cache[n]
    cache[n]=fibonacci_memoization(n-1,cache) +fibonacci_memoization(n-2,cache)
    return cache[n]# recall traversal n+1

# dynamic programming

def fibonacci_dp(n):
    
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


# def fibonacci_dp(n):
    
#     cache = [0,1]
#     i=0


#     while True:

#         if n <=1:
#             return cache[n]
        
#         # tmp = cache[1]
#         # cache[1] =cache[0]+cache[1]
#         # cache[0]=tmp

#         if i<=1:
#             i+=1
#             continue

#         if i==n:
#             return cache[0]+cache[1]

#         tmp = cache[0]
#         cache[0] =cache[1]
#         cache[1]=tmp+cache[1]
#         i+=1

        

        

    




if __name__=="__main__":
    print('divide conquer',fibonacci_dfs_divide_conquer(7))
    cache = {}
    print('memoization',fibonacci_memoization(7,cache))
    print('dynamic',fibonacci_dp(7))