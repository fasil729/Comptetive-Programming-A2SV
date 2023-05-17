# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, parent, grand):
            nonlocal res
            if not root:
                return
            if grand % 2 == 0:
                res += root.val
            dfs(root.left, root.val, parent)
            dfs(root.right, root.val, parent)
        dfs(root, 1, 1)
        return res