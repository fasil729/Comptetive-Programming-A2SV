class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        sum_of_previous = 0
        nums.sort()
        ans = -1
        
        for num in nums:
            if num < sum_of_previous:
                ans = sum_of_previous + num
            sum_of_previous += num
                    
        return ans
            
        