# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def paths(root, path, result):
            if not root.left and not root.right:
                result.append(path)
                return
            if root.left:
                paths(root.left, path + "->" +  str(root.left.val), result)
            if root.right:
                paths(root.right, path + "->"+ str(root.right.val), result)
        path = str(root.val)
        paths(root, path, result)
        return result