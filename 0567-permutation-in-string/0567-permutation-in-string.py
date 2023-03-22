class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original = Counter(s1)
        window_len = Counter()
        for ind, char in enumerate(s2):
            window_len[char] += 1
            if ind >= len(s1):
                if window_len[s2[ind - len(s1)]] == 1:
                    del window_len[s2[ind - len(s1)]]
                else:
                    window_len[s2[ind - len(s1)]] -= 1
            if window_len == original:
                return True
        return False
        