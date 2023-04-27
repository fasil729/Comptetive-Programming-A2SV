class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        store = {}
        for ind, p in enumerate(position):
            store[p] = speed[ind]
        
        res = 0
        position.sort()
        stack = position
        s = store[stack[-1]]
        d = stack[-1]
        while stack:
            p = stack.pop()
    
            t = (target - d) / s
            if stack and ((target - stack[-1]) / store[stack[-1]]) <= t:
                
                continue
            if stack:
                s = store[stack[-1]]
                d = stack[-1]
            res += 1
        return res
                