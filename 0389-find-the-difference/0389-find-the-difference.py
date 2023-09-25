class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = Counter(s)
        for char in count_t:
            if char not in count_s or count_s[char] != count_t[char]:
                return char
        