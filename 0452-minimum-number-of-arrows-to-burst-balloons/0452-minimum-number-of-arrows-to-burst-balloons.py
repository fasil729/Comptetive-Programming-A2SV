class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        mini = points[0][1]
        res = 1
        for point in points:
            if point[0] > mini:
                res += 1
                mini = point[1]
        return res
        