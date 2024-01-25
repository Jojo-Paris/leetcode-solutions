class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        res = 0
        points = sorted(points)
        for i in range(1, len(points)):
            res = max(res, points[i][0] - points[i - 1][0])
        return res
        
        
[
