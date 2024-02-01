class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)

        for i in strs:
            word = ''.join(sorted(i))
            temp[word].append(i)
        
        return temp.values()

        
["eat","tea","tan","ate","nat","bat"]
