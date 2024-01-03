class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = bank[0].count("1")
        
        for row in bank[1:]:
            curr = row.count("1")
            
            if curr:
                ans += curr * prev
                prev = curr
        
        return ans
        