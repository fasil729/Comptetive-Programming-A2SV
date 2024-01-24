# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        visited = set()
        
        def toggle(num, visited):
            if num in visited:
                visited.remove(num)
            else:
                visited.add(num)
        
        def dfs(root):
            if not root:
                return 0
            
            toggle(root.val, visited)
            if not root.left and not root.right:
                if len(visited) <= 1:
                    ans = 1
                else:
                    ans = 0
            else:
                ans = dfs(root.left) + dfs(root.right)
            toggle(root.val, visited)
            
            return ans
        
        return dfs(root)
         
        