class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        def dijkestra(start):
            heap = [(0, start)]
            min_time = {i: inf for i in range(n)}
            min_time[start] = 0

            while heap:
                time, node = heapq.heappop(heap)

                for neigh, path_time in graph[node]:
                    new_time = time + path_time
                    if new_time < min_time[neigh]:
                        heapq.heappush(heap, (new_time, neigh))
                        min_time[neigh] = new_time
                        
            ans = 0
            for dist in min_time.values():
                if dist <= distanceThreshold:
                    ans += 1
            
            return ans
        
        ans = -1
        mini = n
        for city in range(n):
            res = dijkestra(city)
            if mini >= res:
                mini = res
                ans = city
        return ans
            
        