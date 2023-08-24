class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        power = 0
        for num in num1[::-1]:
            res += int(num) * int(num2) * 10 ** power
            power += 1
        return str(res)
        