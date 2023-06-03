# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        def dfs(root, Sum):
            Sum -= root.val
            if not root.left and not root.right:
                return Sum == 0
            res = False
            if root.left:
                res = res or dfs(root.left, Sum)
            if root.right:
                res = res or dfs(root.right, Sum)
            return res
        return dfs(root, targetSum)