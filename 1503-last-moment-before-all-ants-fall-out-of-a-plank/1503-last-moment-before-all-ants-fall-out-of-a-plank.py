class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        if left:
            ans = max(left)
        for r in right:
            ans = max(ans, n - r)
        return ans