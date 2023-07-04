class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = min(tasks)[0]
        heap = []
        ans = []
        n = len(tasks)
        
       
        tasks = sorted([[[task[0], task[1]], i] for i, task in enumerate(tasks)])[::-1]
       
        
        while len(ans) < n:
        
            while tasks and tasks[-1][0][0] <= time:
                    task, i = tasks.pop()
                    heapq.heappush(heap, (task[1], i))
                    
            if heap:
                active = heapq.heappop(heap)
                time += active[0]
                ans.append(active[1])
            else:
                time = tasks[-1][0][0]
           
        return ans 
                
            
        