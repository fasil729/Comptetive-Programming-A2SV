class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        def check_detonate(prev, nex):      
            x_i, y_i, r = bombs[prev]
            x_j, y_j, r_j = bombs[nex]
            d = ((y_j - y_i) ** 2 + (x_j - x_i) ** 2) ** 0.5
            return r >= d # true
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j and check_detonate(i, j):
                     graph[i].append(j)
            
        visited = set() # 0:[1] 1:[0]
          
        def dfs(node):# node = 0
            visited.add(node)
            
            ans = 0
            for neigh in graph[node]:   
                if neigh not in visited:
                    
                    ans += dfs(neigh) 
                    
            return ans + 1
        ans = 0
        for i in range(n):
            visited = set()
            ans = max(ans, dfs(i))
        return ans
                
        
        
        