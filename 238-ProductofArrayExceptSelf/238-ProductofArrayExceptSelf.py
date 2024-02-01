class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = post
            post *= nums[i]

        pre = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pre
            pre *= nums[i]
        return res
[1,2,3,4]
