class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        visited = Counter(s)
        print(visited)
        
        for ind in range(n):
            char = s[ind]
            if visited[char] == 1:
                return ind
        
        return -1
            