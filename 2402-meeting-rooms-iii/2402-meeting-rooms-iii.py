class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = [i for i in range(n)]
        heapify(free_rooms)
        rooms = defaultdict(int)
        reserved_rooms = []
        meetings.sort()
        delayed_time = 0
        
        for meeting in meetings:
            # pop out free rooms from reserved rooms heap
            start, ending = meeting
            while reserved_rooms and reserved_rooms[0][0] <= start:
                _, free = heapq.heappop(reserved_rooms)
                heapq.heappush(free_rooms, free)
            
            # check if there is no free rooms
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(reserved_rooms, (ending, room))
                
            else:
                availble, room = heapq.heappop(reserved_rooms)
                heapq.heappush(reserved_rooms, (availble + ending - start , room))
            rooms[room] += 1
            
        # lets track for the room that held the most meeting
        ans, maxi = -1, 0
        for room in sorted(rooms.keys()):
            if rooms[room] > maxi:
                ans = room
                maxi = rooms[room]
        
        return ans
        
        