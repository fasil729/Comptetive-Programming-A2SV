class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = Counter(s)
        
        values = [[-v, k] for k, v in letters.items()]
        heapq.heapify(values)
        maxi = abs(min(values)[0])
        n = len(s)
        if maxi > ceil(n/2): 
            return ""
        
        ind = 0
        prev = heapq.heappop(values)
        res = prev[1]
        prev[0] += 1
        while values:
            f, char = heapq.heappop(values)
            res += char
            if prev[0] != 0:
                heapq.heappush(values, prev) 
            prev = [f + 1, char]

            
        
        
        return res
        
        