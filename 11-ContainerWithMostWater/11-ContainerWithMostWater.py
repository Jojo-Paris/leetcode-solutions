class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxWater = 0

        l, r = 0, len(height) - 1

        while l < r:

            length = min(height[l], height[r])
            area = length*width
            width = r - l
            
        return maxWater
            if height[l] < height[r]:
                l += 1
            maxWater = max(maxWater, area)
            else:
                r -= 1
            
[
