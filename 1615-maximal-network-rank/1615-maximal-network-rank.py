class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        
        maxi = 0
        for u in range(n):
            for v in range(u + 1, n):
                res = len(graph[v]) + len(graph[u])
                if u in graph[v]:
                    maxi = max(maxi, res - 1)
                else:
                    maxi = max(maxi, res)
        return maxi