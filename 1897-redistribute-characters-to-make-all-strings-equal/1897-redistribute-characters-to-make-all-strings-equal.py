class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        count = defaultdict(int)
        
        for word in words:
            for char in word:
                count[char] += 1
        
        for char in count:
            if count[char] % n:
                return False
        
        return True