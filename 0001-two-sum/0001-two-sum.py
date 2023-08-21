class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach
        n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # hash table approach
        dic = {nums[i]:i for i in range(n)}
        
        for ind in range(n):
            diff = target - nums[ind]
            if diff in dic and ind != dic[diff]:
                return [ind, dic[diff]]
        