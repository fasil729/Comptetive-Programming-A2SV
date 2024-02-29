# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        Prev = []
        
        
        def dfs(root, level):
            if not root:
                return True
            
            if level == len(Prev):
                Prev.append(0)
                if (level + root.val) % 2 == 0:
                    return False
            elif level % 2 == 0 and (root.val % 2 == 0 or Prev[level] >= root.val):
                return False
            elif level % 2 != 0 and (root.val % 2 != 0 or Prev[level] <= root.val):
                return False
            
            Prev[level] = root.val
            
            
            return dfs(root.left, level + 1) and dfs(root.right, level + 1)
        
        return dfs(root, 0)
        