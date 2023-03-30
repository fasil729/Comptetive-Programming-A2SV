# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            node = root.right
            
            while node.left:
                node = node.left
            root.val = node.val
            root.right = self.deleteNode(root.right, node.val) 
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    # def modify_tree(self, root):
    #     if not root:
    #         return 
    #     if not root.left:
    #         value = root.val
    #         # root.left
    #         return value
    #     if not root.left.left:
    #         root.left = root.left.right
    #         return root.left.val
    #     return self.modify_tree(root.left)
            
        