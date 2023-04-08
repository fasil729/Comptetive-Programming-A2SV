# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        
        def helper(start, end):
            if start > end:
                return
            max_num = -1
            ind = 0
            for j in range(start, end + 1):
                if nums[j] > max_num:
                    ind = j
                    max_num = nums[j]
            return TreeNode(nums[ind], helper(start, ind - 1), helper(ind + 1, end))
        return helper(0, len(nums) - 1)
            
                
        