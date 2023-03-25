class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0
        prefsum = []
        for num in nums:
            acc += num
            prefsum.append(acc)
        return prefsum