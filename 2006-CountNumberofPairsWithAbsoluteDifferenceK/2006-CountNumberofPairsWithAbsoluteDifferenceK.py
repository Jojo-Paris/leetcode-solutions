class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        temp = defaultdict(int)
        res = 0
        for i in nums:
            print(temp)
            res += temp[i-k] + temp[i+k]
            print(temp[i-k], temp[i+k])
            temp[i] += 1
        return res
[1,2,2,1]
