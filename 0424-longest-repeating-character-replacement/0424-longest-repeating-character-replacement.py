class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 0
        letters = defaultdict(int)
        for i, char in enumerate(s):
            letters[char] += 1
            res = max(res, self.longestrepating(letters, k, i - start + 1) )
            while start < i and self.longestrepating(letters, k, i - start + 1) == 0:
                letters[s[start]] -= 1
                start += 1
        return res
                
        
        
    def longestrepating(self, letters, k, leng):
        res = 0
        for letter, occ in letters.items():
            if leng - occ <= k:
                res = max(res, leng)
        return res
        
        