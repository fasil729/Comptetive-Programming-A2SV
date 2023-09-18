class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        ans = []
        for ind, row in enumerate(mat):
            arr.append((-1 * row.count(1), -1 * ind))
        heap = []
        for ele in arr:
            heapq.heappush(heap, ele)
            if len(heap) > k:
                heapq.heappop(heap)
            
        while heap:
            freq, ind = heapq.heappop(heap)
            ans.append(-ind)
        return ans[::-1]
        
        