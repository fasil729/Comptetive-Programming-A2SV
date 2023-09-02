class Solution:
    def minExtraChar1(self, s: str, dictionary: List[str]) -> int:
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
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dictionary_set = len(s), set(dictionary)
        @cache
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character 
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            return ans
            
        return dp(0)
                
        