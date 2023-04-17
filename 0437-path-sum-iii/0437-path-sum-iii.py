# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return self.result
        self.helper(root, targetSum)
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.result
    
    
    
    def helper(self, root, target):
            
            
            if not root:
                return
            # print(tot)
            if root.val == target:
                # print(root.val, tot)
                self.result += 1

            self.helper(root.left, target - root.val)
            
            self.helper(root.right, target - root.val)
            
            
            
        