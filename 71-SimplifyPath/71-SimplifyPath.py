class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for i in path:
        res = ''
        path = path.split("/")
            if stack and i == '..': stack.pop()
            elif i not in ['.', '', '..']: stack.append(i)
        
        return "/" + "/".join(stack)
"
