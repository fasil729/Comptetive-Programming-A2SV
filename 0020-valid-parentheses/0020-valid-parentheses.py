class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {"(":")", "{":"}", "[":"]"}
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if stack and bracket[stack.pop()] == char:
                    continue
                return False
        if stack:
            return False
        return True
        