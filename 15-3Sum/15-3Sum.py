class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # -4,-1,-1, 0, 2

        for idx, val in enumerate(nums):

            if val > 0: break
            if idx > 0 and val == nums[idx - 1]: continue
            
            l, r = idx + 1, len(nums)-1
            
            while l < r:
                
                if(val + nums[l] + nums[r]) > 0:
                    r -= 1
                elif(val + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
[-1,0,1,2,-1,-4]
