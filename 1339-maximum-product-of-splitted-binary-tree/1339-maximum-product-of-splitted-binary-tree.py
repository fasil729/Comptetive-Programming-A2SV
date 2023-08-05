# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        @cache
        def tot(root):
            if not root:
                return 0
            return root.val + tot(root.left) + tot(root.right)
        tot_sum = tot(root)
        
        def helper(root, tot_sum):
            nonlocal maxi
            if not root:
                return 
            res = (tot_sum - tot(root)) * tot(root)
            maxi = max(maxi, res)
            helper(root.left, tot_sum)
            helper(root.right, tot_sum)
        
        helper(root, tot_sum)
            
        return maxi % (10 ** 9 + 7)
        
        