class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        leftArr = [0] * len(nums)
        
        for i in range(1, len(nums)):
            leftArr[i] = nums[i - 1] + leftArr[i- 1]
        
        for i in range(len(nums) - 2, -1, -1):
        rightArr = [0] * len(nums)
            rightArr[i] = nums[i + 1] + rightArr[i + 1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):

            res[i] = abs(leftArr[i] - rightArr[i])
        return res
[
