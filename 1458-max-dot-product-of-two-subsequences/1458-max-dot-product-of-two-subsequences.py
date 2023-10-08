class Solution:
    def maxDotProduct1(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        # top down approach
        @cache
        def dp(ind1, ind2):
            if ind1 >= n or ind2 >= m:
                return 0
            
            prod = nums1[ind1] * nums2[ind2]
            
            ans = dp(ind1 + 1, ind2 + 1) + prod
            
            return max(ans, dp(ind1 + 1, ind2), dp(ind1, ind2 + 1))
        
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        return dp(0, 0)
    
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # bottom up approach
        m, n = len(nums2), len(nums1)
        prev_dp = [0] * (m + 1)
        dp = [0] * (m + 1)
        for i in range(n - 1, -1, -1):
            dp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                use = nums1[i] * nums2[j] + prev_dp[j + 1]
                dp[j] = max(use, dp[j + 1], prev_dp[j])
            prev_dp = dp
                
            
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        return dp[0]
            