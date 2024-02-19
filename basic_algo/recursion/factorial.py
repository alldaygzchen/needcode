#  one branch recursion
def factorial_one(n):
    prev_list = [1]*n

    for i in range(1,n):
        prev_list[i] = prev_list[i-1]*(i+1)

    return prev_list[-1]

def factorial_two(n):
    # non recursion 
    prev=1

    for i in range(1,n):
        prev = prev*(i+1)

    return prev

def factorial_three(n):
    # time and space complexity :O(n)
    # space complexity O(n): functions call
    
    if (n<=1):
        return 1
    return n*factorial_three(n-1)



if __name__=="__main__":
    print(factorial_one(3))
    print(factorial_one(5))
    print(factorial_two(3))
    print(factorial_two(5))
    print(factorial_three(3))
    print(factorial_three(5))