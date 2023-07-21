class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        res = 0
        pref = [0]
        for s in satisfaction:
            pref.append(pref[-1] + s)
        count = 0
        for p in pref[1:]:
            count += p
            res = max(res, count)
        return res
                
        