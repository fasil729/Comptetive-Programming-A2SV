# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(left, right, order):
            if not left or not right:
                return
            
            if order % 2 == 1:
                left.val, right.val = right.val, left.val
            dfs(left.left, right.right, order + 1)
            dfs(left.right, right.left, order + 1)
            
        dfs(root.left, root.right, 1)   
        return root
        