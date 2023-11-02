# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root):
            if not root:
                return 0, 0, 0
            
            left_sum, left, left_count = dfs(root.left)
            right_sum, right, right_count = dfs(root.right)
            
            ans = left_count + right_count
            num = left + right + 1
            tot = left_sum + right_sum + root.val
            avg = tot // num
            if root.val == avg:
                ans += 1
            return tot, num, ans
        
        return dfs(root)[2]
        