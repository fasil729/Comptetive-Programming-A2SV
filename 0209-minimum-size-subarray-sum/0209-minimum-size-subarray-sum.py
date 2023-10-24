class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')     
        start = 0
        current_sum = 0    # 5
        
        for end in range(len(nums)):
            current_sum += nums[end]

            while current_sum  >= target and start <= end: 
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1
                
                
        
        if min_length == float('inf'):
            return 0
        return min_length
                
                
        
        