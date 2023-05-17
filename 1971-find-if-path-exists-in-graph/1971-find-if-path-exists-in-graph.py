class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = defaultdict(list)
        for n_1, n_2 in edges:
            adjacency_list[n_1].append(n_2)
            adjacency_list[n_2].append(n_1)
        
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neigh in adjacency_list[node]:
                if not neigh in visited and dfs(neigh):
                    return True
            return False
        return dfs(source)
                
            