def binarySearch(low, high):

    while low <= high:
        mid = (low + high) // 2

        if anonymous_function(mid) > 20:
            high = mid - 1
        elif anonymous_function(mid) < 20:
            low = mid + 1
        else:
            return mid
    return -1

# Return 1 if n is too big, -1 if too small, 0 if correct
def anonymous_function(n):
    return 2*n

if __name__=="__main__":
    print(binarySearch(0,100))