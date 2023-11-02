class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        n = len(graph)
        @cache
        def dfs(node):
            if not graph[node]:
                return True
            if node in visited:
                return False
            visited.add(node)
            ans = True
            for neigh in graph[node]:
                ans = ans and dfs(neigh)
            return ans
        ans = []
        for i in range(n):
            visited = set()
            if dfs(i):
                ans.append(i)
        return ans
        