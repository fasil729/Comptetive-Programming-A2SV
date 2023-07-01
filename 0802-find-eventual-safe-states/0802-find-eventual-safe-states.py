class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        colors = [0 for _ in range(n)]
        order = []

        

        for node in range(n):
            if colors[node] != 0:
                continue
            self.topSort(node, colors, graph, order)
                

        return sorted(order)
    def topSort(self, node, colors, graph, order):
        # Cycle found - Why?
        if colors[node] == 1:
            return False

        colors[node] = 1
        for neighbor in graph[node]:
            if colors[neighbor] == 2:
                continue
            if not self.topSort(neighbor, colors, graph, order):
                return False

        # Color nodes black as we backtrack
        colors[node] = 2
        order.append(node)
        return True
