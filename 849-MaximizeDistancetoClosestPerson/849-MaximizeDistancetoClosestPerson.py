class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        flag = False
        count = 0
        
        for n in seats:
            
            if n == 0:
                count += 1
            else:
                if flag == True:
                    res = max(res, (count+1) // 2)
                else:
                    res = max(res, count)
                    
                count = 0
                flag = True
        return max(res, count)
[1,0,0,0,1,0,1]
