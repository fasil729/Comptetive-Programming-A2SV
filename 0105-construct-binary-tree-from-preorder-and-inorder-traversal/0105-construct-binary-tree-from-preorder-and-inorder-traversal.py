# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        ind = 0
        def helper(start, end):
            nonlocal ind
            if start > end:
                return
            val  = preorder[ind]
            root = TreeNode(val)
            ind += 1
            i = inorder.index(val)
            root.left = helper(start, i - 1)
            root.right = helper(i + 1, end)
            return root
        return helper(0, len(inorder) - 1)
        