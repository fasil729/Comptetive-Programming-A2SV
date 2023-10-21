# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        
        
        def flatten(nestedInteger):
            node = NestedInteger()
            if nestedInteger[0] != "[":
                node.setInteger(int(nestedInteger))
                return node
            child = ""
            stack = []
            for c in nestedInteger[1:-1]:
                if c == "," and not stack:
                    if child:
                        node.add(flatten(child))
                    child = ""
                elif c == "[":
                    stack.append("[")
                    child += c
                elif c == "]":
                    stack.pop()
                    child += c
                else:
                    child += c
            if child:
                node.add(flatten(child))
            return node
        return flatten(s)
                    
                
            