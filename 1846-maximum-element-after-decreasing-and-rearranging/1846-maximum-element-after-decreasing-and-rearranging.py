class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        prev = 0
        
        arr.sort()
        for num in arr:
            if num > prev:
                prev += 1
        return prev