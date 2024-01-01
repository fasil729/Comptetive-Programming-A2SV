class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        ans = -1
        first_ind = {}
        
        for ind, char in enumerate(s):
            if char in first_ind:
                ans = max(ans, ind - first_ind[char] - 1)
            else:
                first_ind[char] = ind
        
        return ans
        