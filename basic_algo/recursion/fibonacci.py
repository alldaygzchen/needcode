
# Recursive implementation to calculate the n-th Fibonacci number
#O(2^n) not O(2n)
def fibonacci(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_iterative(n):
    outputs =[0]*(n+1)
    outputs[0]=0
    outputs[1]=1

    for i in range(2,len(outputs)):
        outputs[i] = outputs[i-1]+outputs[i-2]
    return outputs[n]

################################################################### 
# learn how to write recursion
# the first solution is ideal for divide and conquer

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



def fibonacci_for_loop(target):
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

    return current

# def finonacci_recursion(target,idx=2,prev_prev=0,prev=1):

#     if target==0:
#         return prev_prev
#     if target==1:
#         return prev
#     if target==idx:

#         return prev_prev+prev
    


#     return finonacci_recursion(target,idx+1,prev,prev+prev_prev)

# def fibonacci_for_loop(target):
#     prev_prev=0
#     prev=1

#     if target==0:
#         return prev_prev
#     if target==1:
#         return prev
#     for i in range(2,target+1):
#         current = prev + prev_prev
#         prev_prev = prev
#         prev = current

#     return current


###################################################################


    

if __name__=="__main__":
    print(fibonacci(7))
    # print(fibonacci(8))
    # print(fibonacci(9))
    # print(fibonacci_iterative(7))
    # print(fibonacci_iterative(8))
    # print(fibonacci_iterative(9))
    print(finonacci_recursion(7))
    # print(fibonacci_for_loop(7))