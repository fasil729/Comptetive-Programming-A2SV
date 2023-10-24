# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:   # 
            new_queue = []
            maxi = float("-inf")
            for node in queue:
                maxi = max(node.val, maxi)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            ans.append(maxi)
            queue = new_queue
        
        return ans
        