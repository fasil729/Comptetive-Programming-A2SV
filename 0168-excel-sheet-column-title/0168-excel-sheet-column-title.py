class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        res = ""
        while num:
            num, mod = divmod(num, 26)
            if mod:
                res += chr(ord("A") + mod - 1)
            else:
                res += "Z"
                num -= 1
        return res[::-1]
        