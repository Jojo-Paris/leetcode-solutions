class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def backTrack(idx, arr, total): 

            if total == target:
        res = []
                res.append(arr.copy())
                return 
            if total > target:
                return

            for i in range(idx, len(candidates)):
        backTrack(0, [], 0)
                backTrack(i, arr + [candidates[i]], total + candidates[i])
        return res
[
