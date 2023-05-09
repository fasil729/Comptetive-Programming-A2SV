class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def helper(divisor):
            tot = 0
            for num in nums:
                tot += ceil(num/divisor)
            return tot <= threshold
        start, end = 1, 10**6
        while start <= end:
            mid = start + (end - start) // 2
            if helper(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
        
        
      