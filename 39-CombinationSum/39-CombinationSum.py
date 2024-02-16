class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(arr, idx, totalSum):

        dfs([], 0, 0)

            if totalSum > target:
                return
            if totalSum == target:
                res.append(arr.copy())
            

                return
            
            for i in range(idx, len(candidates)):
                dfs(arr + [candidates[i]], i, totalSum + candidates[i])
        return res
[
