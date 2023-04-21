class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        arr = []
        count = []
        n = len(nums)
        def helper(ind):
            if Counter(arr) not in count:
                res.append(arr.copy())
                count.append(Counter(arr))
            if ind == n:
                return
            arr.append(nums[ind])
            helper(ind + 1)
            arr.pop()
            helper(ind + 1)
        helper(0)
        return res
        