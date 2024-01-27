class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            temp = 0
            while temp < nums[i]:
                res.append(nums[i + 1])
                temp += 1
        
        return res
[1,2,3,4]
