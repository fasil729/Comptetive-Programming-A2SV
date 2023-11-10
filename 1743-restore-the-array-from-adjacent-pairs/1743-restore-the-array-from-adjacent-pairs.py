class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # build graph
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        
        # indentify the end node
        end_node = -1
        for node in graph:
            if len(graph[node]) == 1:
                end_node = node
                break
                
        # traverse the graph either dfs or bfs
        ans = []
        prev = None
        curr = end_node
        
        while curr != prev:
            ans.append(curr)
            temp = curr
            
            
            if graph[curr][0] != prev:
                curr = graph[curr][0]
            elif graph[curr][-1] != prev:
                curr = graph[curr][-1]
            prev = temp
            
        return ans
                
                
        
        
        
        
                