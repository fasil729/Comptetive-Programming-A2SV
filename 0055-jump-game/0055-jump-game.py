class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:return True
        i = 0;j = i
        for i in range(100000):
            if j > i+nums[i]:pass
            else:j = i+nums[i]
            i+=1
            if i > j:break
            if j >= len(nums)-1:return True
        return False
        