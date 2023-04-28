class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = len(nums) + 1
        sum = 0
        heap = [(sum, -1)]
        heapq.heapify(heap)
        for i, num in enumerate(nums):
            sum += num
            while heap:
                pref, ind = heapq.heappop(heap)
                if sum - pref >= k:
                    res = min(res, i - ind)
                else:
                    heapq.heappush(heap, (pref, ind))
                    break
            heapq.heappush(heap, (sum, i))
        
        
        
       
                
        return res if res != len(nums) + 1 else -1
            
            
        