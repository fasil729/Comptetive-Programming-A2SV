class Solution:
    def is_predecessor(self, prev, word):
        for i in range(len(word)):
            sub = word[:i] + word[i + 1:]
            if sub == prev:
                return True
        return False
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key= lambda x: len(x))
        n =  len(words)
        print(n)
        @cache
        def dp(index):
            if index == n - 1:
                return 1
            res = 0
            prev = words[index]
            for ind in range(index + 1, n):
                if len(prev) <= len(words[ind]) - 1 and self.is_predecessor(prev, words[ind]):
                    res = max(res, dp(ind))
            return res + 1
        ans = 0
        for i in range(n):
            ans = max(dp(i), ans)
        return ans
        
        