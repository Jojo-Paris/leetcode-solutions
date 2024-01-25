class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        res = 0

        for idx, arr in enumerate(accounts):

            res = max(res, sum(arr))   
        
        return res
[[1,2,3],[3,2,1]]
