class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build graph
        graph = defaultdict(list)
        
        for pre, co in prerequisites:
            graph[pre].append(co)
            
            
       
        preq = defaultdict(set)
        
        # perform dfs
        def dfs(node):
            if node in preq:
                return preq[node]
            
            ans = set([node])
            for neigh in graph[node]:
                ans |= dfs(neigh)
            preq[node] = ans
            return ans
        for i in range(numCourses):
            dfs(i)
        
        # iterate over queries
        ans = []
        for p, q in queries:
            if q in preq[p]:
                
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
        
        
            

            
            
            
            
            
            
            
            
            
            
            
            
            