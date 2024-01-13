# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        
        while queue:
            new_queue = []
            res = []
            for node in queue:
                res.append(node.val)
                
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                    
            queue = new_queue
            ans.append(res)
        
        return ans
            
                
            
        
        
        