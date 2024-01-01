class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g = [-greed for greed in g]
        s = [-coo for coo in s]

        heapq.heapify(g)
        heapq.heapify(s)
        ans = 0
        
        while s and g:
            coo = -heapq.heappop(s)
            child = -heapq.heappop(g)
            
            while g and coo < child:
                child = -heapq.heappop(g)
                
            if coo >= child:
                ans += 1
        
        
        return ans
            

        