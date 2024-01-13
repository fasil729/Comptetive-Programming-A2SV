class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        visited = set()
        ans = 0
        start, n = 0, len(s)
        
        for end in range(n):
            
            while s[end] in visited:
                visited.remove(s[start])
                start += 1
            
            visited.add(s[end])
            ans = max(ans, end - start + 1)
        
        return ans
        