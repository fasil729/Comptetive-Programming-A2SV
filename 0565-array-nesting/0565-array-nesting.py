class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            return dfs(nums[node]) + 1
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans
        