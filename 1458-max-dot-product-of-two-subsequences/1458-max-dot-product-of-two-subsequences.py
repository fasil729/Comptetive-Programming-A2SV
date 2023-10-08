class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        @cache
        def dp(ind1, ind2):
            if ind1 >= n or ind2 >= m:
                return 0
            ans =  max(dp(ind1 + 1, ind2), dp(ind1, ind2 + 1))
            prod = nums1[ind1] * nums2[ind2]
            ans = max(ans, dp(ind1 + 1, ind2 + 1) + prod)
                
            
            
            return ans
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        return dp(0, 0)
            