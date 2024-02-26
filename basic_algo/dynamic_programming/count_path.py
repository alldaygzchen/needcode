
# suppose there is a matrix, count the path from the top left to the bottom right

# divide and conquer O(2^(n+m))
# no visits
def countpath_divide_conquer(r,c,rows,cols):

    # base case
    if r ==rows or c ==cols:
        return 0
    if r==rows-1 and c==cols-1:
        return 1

    return countpath_divide_conquer(r+1,c,rows,cols)+countpath_divide_conquer(r,c+1,rows,cols)
    
#  O(n*m)
def countpath_memoization(r,c,rows,cols,cache):

    
    # base case
    if r ==rows or c ==cols:
        return 0
    if r==rows-1 and c==cols-1:
        return 1


    # cache
    if cache[r][c]:
        return cache[r][c]


    return countpath_memoization(r+1,c,rows,cols,cache)+countpath_memoization(r,c+1,rows,cols,cache)

#  O(n*m)
def countpath_dp(rows,cols):
    
    prevRow = [1]*cols
    row_id = rows-1-1


    while True:

        if row_id==-1:
            return prevRow[0]
 
        curRow = [0]*cols
        curRow[cols-1] =1
        for c in range(cols-2,-1,-1):
            curRow[c] = curRow[c+1] +prevRow[c]
        prevRow=curRow
        row_id -=1





if __name__=="__main__":
    print('divide conquer',countpath_divide_conquer(0, 0, 4, 4))
    print('top down', countpath_memoization(0, 0, 4, 4,[[None]*4 for i in range(4)]))
    print('dynamic', countpath_dp(4,4))