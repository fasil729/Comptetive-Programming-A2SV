# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        "Bridth first approach"
        if not root:
            return 0
        queue = deque()
        queue.append([root, 1])
        res = 1
        while queue:
            curr =  queue.popleft()
            res = max(res, curr[1])
            if curr[0].left:
                queue.append([curr[0].left, curr[1] + 1])
            if curr[0].right:
                queue.append([curr[0].right, curr[1] + 1])
        return res
            
        