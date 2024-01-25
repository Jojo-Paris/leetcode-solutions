class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        res = 0
        for i, val in enumerate(nums):
            if str(temp).count("1") == k: res += val
            temp = int(bin(i).replace("0b", ""))
        return res
        
[
