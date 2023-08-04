class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word = set(wordDict)
        
        @lru_cache
        def dp(index):
            if index == len(s):
                return True
            path = ""
            res = False
            for i in range(index, len(s)):
                path += s[i]
                if path in word:
                    res = res or dp(i + 1)
            return res
        
        return dp(0)
                    
            