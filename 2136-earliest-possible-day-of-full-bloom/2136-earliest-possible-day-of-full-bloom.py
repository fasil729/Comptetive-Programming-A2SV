class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        new_arr = []
        for ind in range(n):
            new_arr.append((growTime[ind], ind))
        
        new_arr.sort(reverse=True)
        res = 0
        days = 0
        for grow_time, ind in new_arr:
            days += plantTime[ind]
            res = max(days + grow_time, res)
        return res
        