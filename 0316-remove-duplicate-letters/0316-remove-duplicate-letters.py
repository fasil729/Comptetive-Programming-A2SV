class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters = Counter(s)
        stack = []
        for char in s:
            letters[char] -= 1
            if char in stack:
                continue
            while stack and stack[-1] > char and letters[stack[-1]]:
                stack.pop()
            stack.append(char)
        return "".join(stack)