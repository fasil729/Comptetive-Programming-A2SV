class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # consturct graph
        graph = [[] for i in range(n)]
        indegree = [0] * n
        for prev, nex in relations:
            graph[prev - 1].append(nex - 1)
            indegree[nex - 1] += 1
            
        
        # perform topological sort
        ans = max(time)
        stack = [i for i in range(n) if indegree[i] == 0]
        prev_maxi = 0
        maxTime = [time[i] for i in range(n)]
        while stack:
            new_stack = []
            
            for node in stack:
                t = maxTime[node] 
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    maxTime[neigh] = max(maxTime[neigh], t + time[neigh])
                    if indegree[neigh] == 0:
                        ans = max(ans, maxTime[neigh])
                        new_stack.append(neigh)
            stack = new_stack
        return ans 
            
            
        