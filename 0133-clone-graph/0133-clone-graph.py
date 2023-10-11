"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # intialize my visited 
        vis = {}
        
        # do dfs
        def dfs(node):   
            # handle edge case
            if not node:
                return node
            # check if node is in visited
            if node.val in vis:
                return vis[node.val]
            new_node = Node(node.val)
            vis[node.val] = new_node
            adj = []
            
            # itreate through my neioghbours
            for neigh in node.neighbors:
                adj.append(dfs(neigh))
            new_node.neighbors = adj
            return new_node
        
        
        # return my intalize first node
        return dfs(node)
        