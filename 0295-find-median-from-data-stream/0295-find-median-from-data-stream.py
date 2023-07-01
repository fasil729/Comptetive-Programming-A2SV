class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        
        
        if len(self.right_heap) < len(self.left_heap):
            val = heapq.heappushpop(self.left_heap, -1 * num)
            heapq.heappush(self.right_heap, -1 * val) 
        else:
           
            val = heapq.heappushpop(self.right_heap, num)
            heapq.heappush(self.left_heap, -1 * val)
            
        
    def findMedian(self) -> float:
        if len(self.right_heap) == len(self.left_heap):
            return (self.right_heap[0] + -1 * self.left_heap[0]) / 2
        return -1 * self.left_heap[0]    
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()