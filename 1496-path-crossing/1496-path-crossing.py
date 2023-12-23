class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        point = (0, 0)
        visited = set([point])
        
        for direc in path:
            x, y = point
            if direc == "N":
                point = (x, y + 1)
            elif direc == "S":
                point = (x, y - 1)
            elif direc == "E":
                point = (x + 1, y)
            else:
                point = (x - 1, y)
        
            if point in visited:
                return True
            visited.add(point)
        return False
                
        
        