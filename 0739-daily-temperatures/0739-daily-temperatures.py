class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                current = stack.pop()
                res[current] = i - current
            stack.append(i)
        return res
        