# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0, 0
            left_sum, left_ans = dfs(root.left)
            right_sum, right_ans = dfs(root.right)
            tot = left_sum + right_sum
            
            ans = left_ans + right_ans + abs(right_sum - left_sum)
            return tot + root.val, ans
        return dfs(root)[1]
        