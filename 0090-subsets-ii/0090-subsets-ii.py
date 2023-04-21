class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        arr = []
        n = len(nums)
        def helper(ind):
            res.append(arr.copy())
            for i in range(ind, n):
                if i > ind and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                helper(i + 1)
                arr.pop()
        helper(0)
        return res
        