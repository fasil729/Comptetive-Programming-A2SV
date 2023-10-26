class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)
        mod = 10 ** 9 + 7
        @cache
        def dp(root):   # [2, 4]   root = 4   dp [2: 1, 4: 2] 1 + 2 = 3
            ans = 1     # ans = 1
            
            for child in arr:  # 2, 4
                div = int(root/child)  # div = 2
                if root % child == 0 and div in arr:  # 4 % 2 == 0 and 2 in arr
                    ans += dp(child) * dp(div)
            return ans % mod  # 2
        ans = 0
        for root in arr:
            ans += dp(root)
            
        
        return ans % mod
                    
        