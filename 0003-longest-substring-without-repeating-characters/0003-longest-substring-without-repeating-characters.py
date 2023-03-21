class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        res, start = 0, 0
        for ed, char in enumerate(s):
            if char in sub and sub[char] >= start:
                res = max(res, ed - start)
                start = sub[char]
            else:
                res = max(res, ed - start + 1)
            sub[char] = ed + 1
        return res
                
            