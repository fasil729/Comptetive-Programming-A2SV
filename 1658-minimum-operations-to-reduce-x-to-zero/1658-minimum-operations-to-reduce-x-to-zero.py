class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        pref = {}
        tot = 0
        ans = inf
        for ind, num in enumerate(nums):
            tot += num
            pref[tot] = ind + 1
            if tot == x:
                ans = min(ans, ind + 1)
        tot = 0
        for ind, num in enumerate(nums[::-1]):
            tot += num
            ind += 1
            if x == tot:
                ans = min(ind, ans)
            if x - tot in pref and pref[x - tot] + ind <= len(nums):
                ans = min(ans, pref[x - tot] + ind)
        return ans if ans != inf else -1
            
            
            
            