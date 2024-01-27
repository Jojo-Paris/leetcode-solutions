    def countKDifference(self, nums: List[int], k: int) -> int:
        temp = defaultdict(int)
        res = 0
        for i in nums:
            res += temp[i-k] + temp[i+k]
            temp[i] += 1
        return res
class Solution:
[1,2,2,1]
