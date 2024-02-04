class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        l, r, val = 0, 1, 0

        while r < len(prices):
            
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                val = max(val, prices[r] - prices[l])
                r += 1
                
        return val
[7,1,5,3,6,4]
