class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            ans = max(ans, nums[right] + nums[left])
            left += 1
            right -= 1
        
        return ans