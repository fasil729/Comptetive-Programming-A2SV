class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        arr = []
        n = len(nums)
        def backtrack(first, arr):
            if first == n:
                res.append(arr.copy())
                return
            res.append(arr.copy())
            for ind in range(first, n):
                
                arr.append(nums[ind])
                print(arr, first, nums)
                backtrack(ind + 1, arr)
                arr.pop()
               
        backtrack(0, arr)
        return res
            