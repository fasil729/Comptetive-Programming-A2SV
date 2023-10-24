# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        maxi = []
        n = 0
        def dfs(root, depth):
            if not root:
                return depth - 1
            nonlocal n
            n = max(n, root.val)
            if len(maxi) == depth:
                maxi.append([[depth - 1, root.val], depth - 1])
            ans = max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
            
            
            f_maxi, s_maxi = maxi[depth]
            if ans > f_maxi[0]:
                maxi[depth][1] = f_maxi[0]
                maxi[depth][0] = [ans, root.val]
            elif ans > s_maxi:
                maxi[depth][1] = ans
            return ans
        
        dfs(root, 0)
        queue = [root]
        ans = [0] * n
        ind = 0
        while queue:   # 
            new_queue = []
            for node in queue:
                f_maxi, s_maxi = maxi[ind]
                if node.val == f_maxi[1]:
                    ans[node.val - 1] = s_maxi
                else:
                    ans[node.val - 1] = f_maxi[0]
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            ans.append(maxi)
            queue = new_queue
            ind += 1
        res = []
        for q in queries:
            res.append(ans[q - 1])
        return res
            
                    
                
        