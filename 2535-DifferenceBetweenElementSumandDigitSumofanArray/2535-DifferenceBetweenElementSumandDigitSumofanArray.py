class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumRes = sum(nums)
        endRes = 0
        strings = [str(x) for x in nums]
        strings = ''.join(strings)

        for i in strings:
            endRes += int(i)
        
        return abs(sumRes - endRes)
[1,15,6,3]
