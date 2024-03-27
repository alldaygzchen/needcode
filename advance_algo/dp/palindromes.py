# brute force : time complecity O(n^3) 
# solve subproblem first: dynamic programming
# time complexity: O(2n^2)

def longest(s):
    
    length = 0 

    for i in range(len(s)):
        
        # odd situation
        l,r =i,i
        while True:
            if l<0 or r>=len(s) or s[l] != s[r]:
                break
            length = max(r-l+1,length)
            l-=1
            r+=1

        # even situation
        l,r =i,i+1
        while True:
            if l<0 or r>=len(s) or s[l] != s[r]:
                break
            length = max(r-l+1,length)
            l-=1
            r+=1
    return length

# class Solution:

#     def longest_palindromic_substr(self,arrayList):
 
#         # Utility function call
#         k = len(arrayList) - 1
#         return self.longestPalindromic(arrayList, 0, k, 0)
#     # i, j ,count is for the next index since recursion
#     def longestPalindromic(self,arrayList, i, j, count):
#         print(arrayList[i:j+1],i,j,count)
        
#         if i > j :
#             return count
        
#         if i == j :
#             return (count + 1)
            
#         if arrayList[i] == arrayList[j] :
            
#             count = self.longestPalindromic(arrayList, i + 1, j - 1, count + 2)
#             return max(count, max(self.longestPalindromic(arrayList, i, j - 1, 0),self.longestPalindromic(arrayList, i + 1, j, 0)))
        

#         return max( self.longestPalindromic(arrayList, i, j - 1, 0),self.longestPalindromic(arrayList, i + 1, j, 0))
 

# arrayList = ['a','b','a','a','b']
# s= Solution()
# print(s.longest_palindromic_substr(arrayList))
if __name__=="__main__":
    print(longest("abaab"))
