class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def backTrack(idx, arr, total): 

            if total == target:
        res = []
                res.append(arr.copy())
                return 
            if idx >= len(candidates) or total > target:
                return

            arr.append(candidates[idx])
            backTrack(idx, arr, total + candidates[idx])
            arr.pop()
            backTrack(idx + 1, arr, total)
        backTrack(0, [], 0)
        return res
[2,3,6,7]
