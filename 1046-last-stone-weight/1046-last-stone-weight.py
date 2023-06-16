class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * x for x in stones]
        heapify(stones)
        
        while len(stones) > 1:
            y, x = heappop(stones),  heappop(stones)
            diff = y - x
            if diff:
                heappush(stones, diff)
        if stones:
            return -1 * stones[0]
        return 0