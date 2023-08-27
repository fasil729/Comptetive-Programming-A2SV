class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # greedy approach
        pairs.sort(key=lambda x: x[1])
        maxi = 0
        
        res = 1
        last = pairs[0][1]
        for i, j in pairs[1:]:
            if i > last:
                res += 1
                last = j 
    
        return res
    