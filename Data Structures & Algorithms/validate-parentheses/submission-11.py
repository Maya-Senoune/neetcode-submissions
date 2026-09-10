class Solution:
    def isValid(self, s: str) -> bool:

        pairs = { ")":"(", "]":"[" , "}":"{" }
        stack = []


        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop() #pop the top element
                else: 
                    return False

            else: 
                stack.append(c)

        if not stack:
            return True
        else: 
            return False