class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        match = {}
        decode = ""
        for i in key:
            if i not in decode and i !=" ":
                decode += i

        
        for i in range(len(decode)):
            match[decode[i]] = ascii_lowercase[i]
        for i in message:
            if i == " ":
        res = ""
                res += " "
                continue
            else:
                res += match[i]
        
        return res

"
