class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #Input: nums = [1,1,1], k = 2
        #Output: 2

        res = 0
        pre_sum = 0
        d = {0 : 1}

        for n in nums:

            pre_sum = pre_sum + n

            if pre_sum - k in d:
                res = res + d[pre_sum - k]
            
            if pre_sum not in d: d[pre_sum] = 1
            else: d[pre_sum] += 1
        
[1,1,1]
