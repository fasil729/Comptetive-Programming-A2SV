class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for char in s:
            print(stack, res)
            if char == "(":
                    stack.append(0)
            else:
               
                if len(stack) == 1:
                    res += stack[-1] * 2 if stack[-1] else 1
                elif stack and stack[-1]:
                    stack[-2] += 2 * stack[-1]
                elif stack:
                    # print(stack[-2], stack[-1])
                    stack[-2] += stack[-1] + 1
                stack.pop()
        return res
                   
                    