class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0

        for r in range(len(s)):
            window = s[l:r + 1]
            if window.count(s[r]) > 1:
                l = s.find(s[r], l) + 1
            else:
                res = max(res, r - l + 1)
        
        return res
            



            
            


"abcabcbb"
