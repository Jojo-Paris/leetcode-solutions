class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: 
str) -> int:

        res = 0

        if ruleKey == "color": temp = 1
        elif ruleKey == "name": temp = 2
        else: temp = 0

        for i in items:
[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold",
