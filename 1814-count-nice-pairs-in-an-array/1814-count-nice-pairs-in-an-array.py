class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(x):
            x = str(x)
            return int(x[::-1])
        diff = defaultdict(int)
        mod = 10 ** 9 + 7
        
        for num in nums:
            diff[num - rev(num)] += 1
            
        ans = 0
        for num in diff:
            val = diff[num]
            ans += val * (val - 1) // 2
            
        return ans % mod
            
        