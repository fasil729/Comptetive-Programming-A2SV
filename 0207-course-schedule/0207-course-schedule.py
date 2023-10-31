class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #build graph
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for pre, cou in prerequisites:
            graph[pre].append(cou)
            indegree[cou] += 1
            
        queue = [i for i in range(numCourses) if indegree[i] == 0]
    
        while queue:
            new_queue = []
            for node in queue:
                numCourses -= 1
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        new_queue.append(neigh)
            queue = new_queue
        
        return numCourses == 0
        