class Solution:
    def shortestPathLength1(self, graph: List[List[int]]) -> int:
        visited = defaultdict(int)
        for i, adj in enumerate(graph):
            visited[i] = len(adj)
        path = []
        ans = float("inf")
        n = len(graph)
        def dfs(node):
            nonlocal ans
            if len(set(path)) == n:
                # print(path, ans)
                ans = min(ans, len(path))
                return
            if not visited[node]:
                return
            visited[node] -= 1
            path.append(node)
            for neigh in graph[node]:
                
                dfs(neigh)
            path.pop()
            visited[node] += 1
        for i in range(n):
            dfs(i)
        return ans - 1 if ans != inf else 0
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(1 << i, i, 0) for i in range(n)])
        visited = set((1 << i, i) for i in range(n))
        
        while queue:
            mask, node, dist = queue.popleft()
            if mask == (1 << n) - 1:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, dist + 1))
                
        