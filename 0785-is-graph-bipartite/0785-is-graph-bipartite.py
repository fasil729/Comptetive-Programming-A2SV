class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(node):
            
            for neigh in graph[node]:
                if neigh in color:
                    if color[neigh] == color[node]:
                        return False
                    continue
                color[neigh] = 1 - color[node]
                
                if not dfs(neigh):
                    return False
            return True
        
        color = {}
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False
        return True
                
        
        