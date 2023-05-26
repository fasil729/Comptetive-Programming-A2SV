class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set([0])
        
        queue = deque([0])
        
        while queue:
            room = queue.popleft()
            
            for neigh in rooms[room]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)
        if len(visited) == n:
            return True
        return False
        