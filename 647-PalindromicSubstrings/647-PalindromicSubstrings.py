class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
    

        for i in range(len(s)):
            res += self.singlePalindrome(s, i, i)
            res += self.singlePalindrome(s, i, i + 1)
    def singlePalindrome(self,s, l, r):
        
        return res
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
            
        return res
"abc"
