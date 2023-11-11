class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for v, u, cost in edges:
            self.graph[v].append((u, cost))
        

    def addEdge(self, edge: List[int]) -> None:
        v, u, cost = edge
        self.graph[v].append((u, cost))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        
        heap = [(0, node1)]
        visited = [inf for _ in range(len(self.graph))]
        while heap:
            cost, node = heapq.heappop(heap)
            if node == node2:
                return cost
            
            for neigh, c in self.graph[node]:
                new_cost = cost + c
                if new_cost < visited[neigh]:
                    visited[neigh] = new_cost
                    heapq.heappush(heap, (new_cost, neigh))
                
        return -1
        
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)