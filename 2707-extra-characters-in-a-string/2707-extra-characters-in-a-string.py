class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # top down dp
        n = len(s)
        dictionary = set(dictionary)
        @cache
        def dp(index, extra):
            if index >= n:
                return extra
            temp = ""
            res = n - index
            for i in range(index, n):
                temp += s[i]
                for j in range(len(temp)):
                    if temp[j:] in dictionary:
                        res = min(res, dp(i + 1, j))
                        break
                        
            return extra + res
        return dp(0, 0)
                    
                
        