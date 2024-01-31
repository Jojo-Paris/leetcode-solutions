class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s: return True
        
        l, r = 0, len(s) - 1
        
        while l < r:
            
            if s[l] != s[r]:
                sLeft, sRight = s[l + 1: r + 1], s[l: r]
                return(sLeft[::-1] == sLeft or sRight[::-1] == sRight)
            
            l+=1
            r-=1
            
        return True
        
"aba"
