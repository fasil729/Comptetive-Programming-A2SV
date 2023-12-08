# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ""
        
        ans = str(root.val)
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        if not left and not right:
            return ans
        if not right:
            return ans + "(" + left + ")"
        
        return ans + "(" + left + ")" + "(" + right + ")"
        
        