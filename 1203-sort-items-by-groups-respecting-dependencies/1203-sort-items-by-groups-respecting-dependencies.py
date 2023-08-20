class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        # assign group for ungrouped ones
        num = m
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        groups = [[] for i in range(m)]
        item_graph = defaultdict(set)
        group_graph = defaultdict(list)
        item_indegree = [0 for i in range(n)]
        group_indegree = [0 for i in range(m)]
        
        # building the graph
        for ind, g in enumerate(group):
            for b in beforeItems[ind]:
                item_graph[b].add(ind)
                
                item_indegree[ind] += 1
                if g != group[b]:
                    group_graph[group[b]].append(g)
                    group_indegree[g] += 1
        
        # implement topological sort for item_graph
        visited = set()
        queue = deque()
        
        # add indegree 0 nodes
        for ind, item in enumerate(item_indegree):
            if item == 0:
                queue.append(ind)
            
        while queue:
            node = queue.popleft()
            visited.add(node)
            groups[group[node]].append(node)
            for neigh in item_graph[node]:
                item_indegree[neigh] -= 1
                if item_indegree[neigh] == 0:
                    queue.append(neigh)
        if len(visited) != len(item_graph):
            return []
        print(groups)
        print(item_graph)
        # implement topological sort for group_graph
        visited = set()
        ans = []
        queue = deque()
        
        # add indegree 0 nodes
        for ind, item in enumerate(group_indegree):
            if item == 0:
                queue.append(ind)

        while queue:
            node = queue.popleft()
            visited.add(node)
            ans.extend(groups[node])
            for neigh in group_graph[node]:
                group_indegree[neigh] -= 1
                if group_indegree[neigh] == 0:
                    queue.append(neigh)
        if len(visited) != len(group_graph):
            return []
        return ans
                
        
        
        
        
            