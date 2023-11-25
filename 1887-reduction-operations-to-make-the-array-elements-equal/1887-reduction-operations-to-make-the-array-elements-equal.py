class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0
        n = len(nums)
        prev = 1
        for ind in range(1, n):
            if nums[ind] != nums[ind - 1]:
                ans += prev
            prev += 1
        return ans
        
        