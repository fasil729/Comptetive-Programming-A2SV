class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        tails = defaultdict(list)

        for n in nums:
            if tails[n - 1]:
                heappush(tails[n], heappop(tails[n - 1]) + 1)
            else:
                heappush(tails[n], 1)

        return all(
            l >= 3
            for tail in tails.values()
            for l in tail
        )