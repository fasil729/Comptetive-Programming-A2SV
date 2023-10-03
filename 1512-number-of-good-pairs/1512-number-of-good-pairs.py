class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        visited = defaultdict(int)
        ans = 0
        for num in nums:
            ans += visited[num]
            visited[num] += 1
        return ans
        