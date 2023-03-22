class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        beg, tot = 0, 0
        for ed in range(len(nums)):
            tot += nums[ed]
            while beg < len(nums) and tot >= target:
                res = min(res, ed - beg + 1)
                tot -= nums[beg]
                beg += 1
            ed += 1
        return 0 if res == len(nums) + 1 else res