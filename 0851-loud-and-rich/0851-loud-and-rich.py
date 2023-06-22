class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)
            
        answer = [None] * n
       
        def dfs(node):
            
            if answer[node] is None:
                pot = node
                for neigh in graph[node]:
                    
                    cand = dfs(neigh)
                    if quiet[cand] < quiet[pot]:
                        pot = dfs(neigh)
                answer[node] = pot
               
            return answer[node]
        for i in range(n):
            dfs(i)
        return answer
                    
                    
                    
                    