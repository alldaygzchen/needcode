
#O(2^n) not O(2n)
def fibonacci_dfs_divide_conquer(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    return fibonacci_dfs_divide_conquer(n - 1) + fibonacci_dfs_divide_conquer(n - 2)

def fibonacci_dp(n):
    outputs =[0]*(n+1)
    outputs[0]=0
    outputs[1]=1

    for i in range(2,len(outputs)):
        outputs[i] = outputs[i-1]+outputs[i-2]
    return outputs[n]

################################################################### 
# learn how to write recursion

def finonacci_recursion(target,idx=0,prev_prev=None,prev=None):

    if target==0:
        return prev_prev
    if target==1:
        return prev
    
    if idx == 0:
        return finonacci_recursion(target,idx+1,None,0)    
    
    if idx == 1:
        return finonacci_recursion(target,idx+1,0,1)


    if target==idx:

        return prev_prev+prev
    


    return finonacci_recursion(target,idx+1,prev,prev+prev_prev)



def fibonacci_while_loop(target):
    prev_prev=0
    prev=1
    i=0


    # for i in range(target+1):
    while (True):

        if target==0:
            return prev_prev

        if target==1:
            return prev
        
        if i in (0,1):
            i+=1
            continue

        if i==target:
            return prev + prev_prev
        

        current = prev + prev_prev
        prev_prev = prev
        prev = current
        i+=1



###################################################################


    

if __name__=="__main__":
    print(fibonacci_dfs_divide_conquer(7))
    print(fibonacci_dfs_divide_conquer(8))
    print(fibonacci_dfs_divide_conquer(9))
    print(fibonacci_dp(7))
    print(fibonacci_dp(8))
    print(fibonacci_dp(9))
    # print(finonacci_recursion(7))
    # print(fibonacci_while_loop(7))