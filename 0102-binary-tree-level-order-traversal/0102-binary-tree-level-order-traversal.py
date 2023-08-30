# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertOrder(self,root,res,pointer):
        if root!=None:
            self.res[pointer].append(root.val)
            self.insertOrder(root.left,self.res,pointer+1)
            self.insertOrder(root.right,self.res,pointer+1)
        return self.res
            
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = defaultdict(list)
        pointer = 0
        self.insertOrder(root,self.res,pointer)
        return self.res.values()
        