        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] == target: return mid
            if nums[l] <= nums[mid]:
        
        return -1
                if target > nums[mid] or target < nums[l]: l = mid + 1

                else: r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]: r = mid - 1
                else: l = mid + 1

    def search(self, nums: List[int], target: int) -> int:
class Solution:
[4,5,6,7,0,1,2]
