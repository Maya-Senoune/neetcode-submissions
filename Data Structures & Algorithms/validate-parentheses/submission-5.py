class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in pairs.values():        # opening bracket
                stack.append(char)
            elif char in pairs:                # closing bracket
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        
        return not stack