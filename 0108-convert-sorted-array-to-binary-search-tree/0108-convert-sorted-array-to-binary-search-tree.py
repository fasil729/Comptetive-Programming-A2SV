# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def helper(start, end):
            if start >= end:
                return
            mid = start + (end - start) // 2
    
            return TreeNode(nums[mid], helper(start, mid), helper(mid + 1, end))

        return helper(0, len(nums))
    
            