class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        pref = [0]
        n = len(nums)
        for num in nums:
            pref.append(pref[-1] + num)
            
        
        def is_possible(f):
            
            for ind in range(f, n + 1):
                tot = pref[ind] - pref[ind - f]
                num = nums[ind - 1]
                if (num * f) - tot <= k:
                    return True
            return False
        
        l, r = 1, n
        while l <= r:
            mid = (r + l) // 2
            if is_possible(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
        
                
                
            
            
            

        