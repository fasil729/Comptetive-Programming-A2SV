class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = set()
        ans = set()
        temp = ""
        for char in s:
            temp += char
            if len(temp) == 10:
                if temp in visited:
                    ans.add(temp)
                visited.add(temp)
                temp = temp[1:]
        return list(ans)
            
        
        