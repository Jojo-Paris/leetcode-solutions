class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx, val in enumerate(nums):
            output = target - val
        Hash = {}


            if output in Hash: return [Hash[output], idx]
            else: Hash[val] = idx
        
        return -1

[
