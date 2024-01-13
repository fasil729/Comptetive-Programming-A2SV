# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
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
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        ans = []
        
        
        def dfs(root, level):
            if not root:
                return
            
            if level == len(ans):
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            
        dfs(root, 0)
        return ans
            
                
            
        
        
        