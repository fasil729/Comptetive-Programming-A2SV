# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, 0
            
            left_depth, left= dfs(root.left)
            right_depth, right = dfs(root.right)
            return max(right_depth, left_depth) + 1, max(right, left, left_depth + right_depth)
        
        return dfs(root)[1]
        