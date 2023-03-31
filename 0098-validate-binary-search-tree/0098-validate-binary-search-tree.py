# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def is_valid(root, maxi, mini):
            if not root:
                return True
            if mini < root.val < maxi:
                return is_valid(root.left, root.val, mini) and is_valid(root.right, maxi, root.val)
            return False
        return is_valid(root, inf, -inf)