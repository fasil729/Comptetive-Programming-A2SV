class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        ans = 0
        
        def isGood(word):
            word_count = Counter(word)
            for char in word_count:
                if char not in chars_count or chars_count[char] < word_count[char]:
                    return 0
            return len(word)
        
        for word in words:
            ans += isGood(word)
            
        
        return ans
            
            
        
            
        