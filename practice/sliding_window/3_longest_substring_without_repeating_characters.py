class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        overall_longest = 0
        hashset = set()
        while True:

            if r == len(s):
                return overall_longest
            
            if s[r] not in hashset:
                hashset.add(s[r])
                overall_longest = max(overall_longest,r-l+1)
            
            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l+=1
                hashset.add(s[r])
                overall_longest = max(overall_longest,r-l+1)
            r+=1

            



if __name__=="__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb")) #3
    print(s.lengthOfLongestSubstring("bbbbb")) #1
    print(s.lengthOfLongestSubstring("pwwkew")) #3
