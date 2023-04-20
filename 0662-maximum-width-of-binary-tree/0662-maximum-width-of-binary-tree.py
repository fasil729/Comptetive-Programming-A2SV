# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        count = {}
        res = 1
        
        def helper(root, level, col):
            nonlocal res
            if not root:
                return
            if level in count:
                tup = count[level]
                count[level] = (min(tup[0], col), max(tup[1], col))
            else:
                count[level] = (col, col)
            tup = count[level]
            res = max(res, tup[1] - tup[0] + 1)
            helper(root.left, level + 1, 2 * col)
            helper(root.right, level + 1, 2 * col + 1)
        helper(root, 1, 0)
        return res

            
        
        