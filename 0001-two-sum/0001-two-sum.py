class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n**2)
        n = len(nums)
        for ind in range(n):
            for j in range(ind + 1, n):
                if nums[j] + nums[ind] == target:
                    return [ind, j]
    
    
            
        