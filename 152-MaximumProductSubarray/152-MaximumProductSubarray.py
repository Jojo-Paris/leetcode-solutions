class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        curMin, curMax = 1, 1

        for i in nums:
            
            temp = curMax
            curMax = max(i * curMax, i * curMin, i)
            curMin = min(i * temp, i * curMin, i)

            res = max(curMax, res)
        return res

[2,3,-2,4]
