class Solution:
    def minOperations(self, s: str) -> int:
        
        
        def countMisplaced(start):
            
            count = 0
            curr = start
            for char in s:
                if char != str(curr):
                    count += 1
                curr = 1 - curr
            
            return count
        
        return min(countMisplaced(0), countMisplaced(1))
                    