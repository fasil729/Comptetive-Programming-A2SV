class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = float("inf")
        start, last = 0, -4
        while start <= 3:
            res = min(res, nums[last] - nums[start])
            start += 1
            last += 1
        return res 
        