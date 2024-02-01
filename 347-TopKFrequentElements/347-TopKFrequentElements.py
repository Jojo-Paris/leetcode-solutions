class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)] 
        res = []

        for key, val in count.items():
            bucket[val].append(key)
        
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                res.append(j)
            if len(res) == k: return res
            

       


[1,1,1,2,2,3]
