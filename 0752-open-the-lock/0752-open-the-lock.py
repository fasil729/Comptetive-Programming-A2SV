class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)
        if "0000" in dead:
            return -1
        
        queue = deque([("0000", 0)])
        visited = set()
        
        while queue:
            state, count = queue.popleft()
            
           
            if state == target:
                return count
            for i in range(4):
                up = (int(state[i]) + 1) % 10
                down = (int(state[i]) - 1) % 10
                state_up = state[0:i] + str(up) + state[i+1:]
                state_down = state[0:i] + str(down) + state[i+1:]
                if state_up not in dead and state_up not in visited:
                    queue.append((state_up, count + 1))
                if state_down not in dead and state_down not in visited:
                    queue.append((state_down, count + 1))
                visited.add(state_up)
                visited.add(state_down)
            
        return -1
            