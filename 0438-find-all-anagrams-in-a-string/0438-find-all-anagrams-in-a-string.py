class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        origin = Counter(p)
        window = Counter(s[:len(p) - 1])
        res = []
        for ind in range(len(p) - 1, len(s)):
            window[s[ind]] += 1
            if window == origin:
                res.append(ind - len(p) + 1)
            window[s[ind - len(p) + 1]] -= 1
        return res
                