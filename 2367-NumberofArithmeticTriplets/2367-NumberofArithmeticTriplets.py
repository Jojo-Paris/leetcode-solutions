class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        m = {}
        for i, n in enumerate(nums):
            if n-diff in m and n-diff*2 in m:
                res += 1
            m[n] = 1
        return res
[
