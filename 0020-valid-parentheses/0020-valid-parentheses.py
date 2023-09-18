class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"{":"}", "(":")", "[":"]"}
        for b in s:
            if b in brackets:
                stack.append(b)
            elif stack and brackets[stack[-1]] == b:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
        