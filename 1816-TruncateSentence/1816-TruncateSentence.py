class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        temp = s.split(" ")
        return ' '.join(temp[0:k])
        
"Hello how are you Contestant"
