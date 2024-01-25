class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #loop through once to end of array
        #save all numbers i find in a hashmap with that index
        #if i subtract the target the a number and it is not in that hashmap we have not found it yet
        #thus we need to add it inside, if it is found we return both the indices

        n = len(nums)
        temp = {}

        for idx, val in enumerate(nums):
            remainder = target - val

            if remainder in temp:
                return [temp[remainder], idx]
            else:
                temp[val] = idx
        
        return None
[2,7,11,15]
