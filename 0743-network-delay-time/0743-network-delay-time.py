class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        
        heap = [(0, k)]
        min_time = {i: inf for i in range(1, n + 1)}
        min_time[k] = 0
        
        while heap:
            time, node = heapq.heappop(heap)
            
            for neigh, path_time in graph[node]:
                new_time = time + path_time
                if new_time < min_time[neigh]:
                    heapq.heappush(heap, (new_time, neigh))
                    min_time[neigh] = new_time
        
        ans = max(min_time.values())
        if ans == inf:
            return -1
        return ans
                
        