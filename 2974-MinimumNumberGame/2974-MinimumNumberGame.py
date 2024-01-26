class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)
        for i in range(1, len(nums), 2):
            
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

        return nums

[5,4,2,3]
