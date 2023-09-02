class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # top down dp
        n = len(s)
        dictionary = set(dictionary)
        @cache
        def dp(index):
            if index >= n:
                return 0
            temp = ""
            res = n - index
            for i in range(index, n):
                temp += s[i]
                for j in range(len(temp)):
                    if temp[j:] in dictionary:
                        res = min(res, dp(i + 1) + j)
                        
            return res
        return dp(0)
                    
                
        