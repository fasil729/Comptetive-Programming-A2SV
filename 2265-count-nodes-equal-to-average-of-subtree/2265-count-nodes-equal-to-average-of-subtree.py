# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root:
                return 0, 0, 0
            res_l, sum_left, n_l = helper(root.left) 
            res_r, sum_right, n_r = helper(root.right)
            n = n_l + n_r + 1
            res = res_l + res_r
            tot = sum_left + sum_right + root.val 
            new_av = tot // n
            if new_av == root.val:
                res += 1
            return res, tot, n
        return helper(root)[0]