class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {"(" : ")", "{" : "}", "[" : "]"}
        
        for c in s:
            if c in close:  
                stack.append(c)
            else:  
                if stack and close[stack[-1]] == c:  
                    stack.pop()
                else:
                    return False

        return not stack  
