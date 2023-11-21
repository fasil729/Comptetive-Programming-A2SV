class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(x):
            x = str(x)
            return int(x[::-1])
        diff = defaultdict(int)
        mod = 10 ** 9 + 7
        ans = 0
        for num in nums:
            d = num - rev(num)
            ans += diff[d]
            diff[d] += 1
            
       
        return ans % mod
            
        