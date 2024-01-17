class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count = Counter(arr)
        n = len(count)
        
        if len(set(count.values())) == n:
            return True
        
        return False
        
        
        