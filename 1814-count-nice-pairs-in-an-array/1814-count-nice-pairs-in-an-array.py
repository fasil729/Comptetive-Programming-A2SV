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
        for num in nums:
            ans += diff[num - rev(num)] - 1
            
        return ans // 2 % mod
            
        