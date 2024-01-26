class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = []

        while nums:
            aliceMin = min(nums)
            nums.remove(aliceMin)
            bobMin = min(nums)
            nums.remove(bobMin)


            res.append(bobMin)
            res.append(aliceMin)
        
        return res
            
[5,4,2,3]
