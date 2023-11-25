class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        n = len(nums)
        prev = 0
        for num, val in sorted(count.items())[n:0:-1]:
            # print(num, val)
            prev += val
            ans += prev
        return ans
        
        