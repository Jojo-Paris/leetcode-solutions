
        l, r, res = 0, len(nums) - 1, 0

        while l < r:
            if nums[l] + nums[r] < target:
        #[-1,1,1,2,3]
                res += r - l
                l += 1
            else:
                r -= 1
        return res
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()
[-1,1,2,3,1]
