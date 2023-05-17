"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        mapped = {e.id:e for e in employees}
        
        def dfs(emp):
            res = emp.importance
            for sub in emp.subordinates:
                res += dfs(mapped[sub])
            return res
        return dfs(mapped[id])
        
        