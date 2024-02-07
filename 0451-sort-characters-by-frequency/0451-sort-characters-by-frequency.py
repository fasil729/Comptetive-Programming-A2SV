class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        ans = ""
        freq = [(value, key) for key, value in count.items()]
        
        for freq, char in sorted(freq):
            ans = (freq * char) + ans
            
            
        return ans
        