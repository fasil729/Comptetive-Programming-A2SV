class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        ans = []
        n = len(nums)
        
        def backtrack(mask, sub):
            if mask in visited:
                return
            ans.append(sub.copy())
            visited.add(mask)
            
            for i in range(n):
                if mask & 1 << i:
                    sub.append(nums[i])
                    backtrack(mask ^ 1 << i, sub)
                    sub.pop()
            return
        backtrack((2 ** n) - 1, [])
        return ans
        