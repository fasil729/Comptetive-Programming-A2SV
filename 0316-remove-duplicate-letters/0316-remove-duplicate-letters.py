class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        ans = ""
        stack = []
        visited = set()
        for char in s:
            count[char] -= 1
            if char in visited:
                continue
            while stack and stack[-1] > char and count[stack[-1]] != 0:
                visited.remove(stack[-1])
                stack.pop()
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)
