class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        path = [0]
        visited = set()
        def dfs(node):
            if node == n - 1:
                res.append(path.copy())
                return
#             if node in visited:
#                 return
            
#             visited.add(node)   
            for neigh in graph[node]:
                path.append(neigh)
                dfs(neigh)
                path.pop()
        
        dfs(0)
        return res