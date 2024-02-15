class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backTrack(idx, arr, total): 
            if total == target:
                res.append(arr.copy())
                return 
            if total > target:
                return

            for i in range(idx, len(candidates)):
                backTrack(i, arr + [candidates[i]], total + candidates[i])

        backTrack(0, [], 0)
        return res
[2,3,6,7]
