class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decre = 0
        incre = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                incre += 1
                decre += 1
            elif nums[i] < nums[i - 1]:
                decre += 1
            else:
                incre += 1
        return incre == n - 1 or decre == n - 1
            
        