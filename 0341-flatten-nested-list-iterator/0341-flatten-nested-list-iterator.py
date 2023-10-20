# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.ind = 0
        
        for nestInteger in nestedList:
            self.dfs(nestInteger)
        self.n = len(self.arr)
    def dfs(self, nestedInteger):
        if nestedInteger.isInteger():
            self.arr.append(nestedInteger.getInteger())
        else:
            for node in nestedInteger.getList():
                self.dfs(node)
        
        
        
    
    def next(self) -> int:
        ans = self.arr[self.ind]
        self.ind += 1
        return ans
        
    
    def hasNext(self) -> bool:
        return self.ind < self.n
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())