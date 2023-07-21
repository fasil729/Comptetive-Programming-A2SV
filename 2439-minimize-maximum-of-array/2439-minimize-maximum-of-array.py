class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot = 0
        res = 0
        ind = 0
        for num in nums:
            tot += num
            ind += 1
            res = max(res, math.ceil(tot/ind))
        return res