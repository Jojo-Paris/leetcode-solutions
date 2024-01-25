class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0

        for i in sentences:
            res = max(i.count(" ") + 1, res)
        return res

["alice and bob love leetcode","i think so too","this is great thanks very much"]
