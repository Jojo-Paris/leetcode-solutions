class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        currMax = max(candies)

        for i in candies:
            if (i + extraCandies) >= currMax: res.append(True)
            else: res.append(False)

        return res
[2,3,5,1,3]
