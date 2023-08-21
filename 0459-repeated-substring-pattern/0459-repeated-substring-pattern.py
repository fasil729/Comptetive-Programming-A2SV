class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp = ""
        n = len(s)
        for char in s[:n//2]:
                temp += char
                c = len(temp)

                if temp + (n  - c) // c * temp == s:
                    return True
        return False
        