class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(isConnected)):
                for j in range(len(isConnected[0])):
                    if isConnected[i][j]:
                        graph[i].append(j)
                        graph[j].append(i)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh in graph[node]:
                dfs(neigh)
        res = 0
        for node in graph:
            if node in visited:
                continue
            dfs(node)
            res += 1
        return res
            

        