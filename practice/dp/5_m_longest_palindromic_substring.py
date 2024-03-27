class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        length = 0 
        substring = ""
        
        for i in range(len(s)):
            
            # odd situation
            l,r =i,i
            while True:
                if l<0 or r>=len(s) or s[l] != s[r]:
                    break
                length = max(r-l+1,length)
                if length == r-l+1:
                    substring = s[l:r+1]
                l-=1
                r+=1

            # even situation
            l,r =i,i+1
            while True:
                if l<0 or r>=len(s) or s[l] != s[r]:
                    break
                length = max(r-l+1,length)
                if length ==r-l+1:
                    substring = s[l:r+1]
                l-=1
                r+=1
        
        return substring


if __name__=="__main__":
    s = Solution()
    print(s.longestPalindrome("abaab"))