class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot = 0
        beg, ed = 0, 0
        res = sum(nums[0:k])
        while ed < len(nums):
            tot += nums[ed]
            if ed - beg == k - 1:
                res = max(res, tot)
                tot -= nums[beg]
                beg += 1
            ed += 1
        return res / k
                
            
    