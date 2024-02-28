# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = -1
        max_level = -1       
        def dfs(root, level):
            nonlocal ans, max_level
            if not root:
                return 
            
            
            if level > max_level:
                ans = root.val
                max_level = level
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            
        
        dfs(root, 0)
        return ans

                
            
            
        