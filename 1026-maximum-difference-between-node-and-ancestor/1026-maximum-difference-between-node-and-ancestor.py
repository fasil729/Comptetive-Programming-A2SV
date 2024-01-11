# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        def dfs(root, maxi, mini):
            nonlocal ans
            
            ans = max(ans, maxi - mini)
            
            if not root:
                return
            
            maxi = max(maxi, root.val)
            mini = min(mini, root.val)
            
            dfs(root.left, maxi, mini)
            dfs(root.right, maxi, mini)
            
        dfs(root, 0, inf) 
        return ans