class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        i = 0
        
        def helper(ind):
            nonlocal i
            res = ""
            i = ind
            while i < n:
                num = 0
                while "0" <= s[i] <= "9":
                    num = (num * 10) + int(s[i])
                    i += 1
                if s[i] == "[":
                    i += 1
                    res += int(num) * helper(i)
                elif s[i] == "]":
                    i += 1
                    break
                else:
                    res += s[i]
                    i += 1
            return res   
        return helper(0)
            
        