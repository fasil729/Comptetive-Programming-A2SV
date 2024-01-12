class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        VOWELS = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        n = len(s)
        count = 0
        
        for ind in range(n):
            if s[ind] in VOWELS:
                if ind < n // 2:
                    count += 1
                else:
                    count -= 1
        
        return count == 0
        