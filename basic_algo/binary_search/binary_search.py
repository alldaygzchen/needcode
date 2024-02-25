
arr = [1, 3, 3, 4, 5, 6, 7, 8]


def binarySearch(arr, target):

    L, R = 0, len(arr) - 1
    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid
    return -1


##################################################

def binarySearchRecursive(arr,target,l,r):

    if l<=r:

        mid = (l + r) // 2
        if target > arr[mid]:
            return binarySearchRecursive(arr,target,mid+1,r)
        if target > arr[mid]:
            return binarySearchRecursive(arr,target,l,mid-1)
        return mid
    return -1




if __name__=="__main__":
    print(binarySearch(arr, 4))
    print(binarySearchRecursive(arr, 4,0,len(arr)-1))