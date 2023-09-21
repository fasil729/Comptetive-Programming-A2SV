class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        mapped = list(zip(scores, ages))
        mapped.sort(reverse=True)
        n = len(scores)
        @cache
        def dp(index):
            if index == n:
                return 0
            curr_score, curr_age = mapped[index]
            ans = curr_score
            for ind in range(index + 1, n):
                score, age = mapped[ind]
                if age <= curr_age or score == curr_score:
                    ans = max(ans, dp(ind) + curr_score)
            return ans
        res = 0
        for i in range(n):
            res = max(res, dp(i))
        return res
        