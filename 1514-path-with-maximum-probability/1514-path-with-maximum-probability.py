class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        # build graph
        graph = [[] for i in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[v].append((u, prob))
            graph[u].append((v, prob))
        
        max_heap = [(-1, start_node)]
        visited = set()
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            visited.add(node)
            if node == end_node:
                return -prob
            for neigh, p in graph[node]:
                new_prob = prob * p
                if neigh not in visited:
                    heapq.heappush(max_heap, (new_prob, neigh))
        return 0
                    
        
        