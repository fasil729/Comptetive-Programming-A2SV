# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def backtrack(n, maxi, mini):
            # if maxi <= mini:
            #     return [TreeNode(n)]
            if n in visited:
                return []
            visited.add(n)
            res = []
            lefts, rights = [], []
            for i in range(mini, maxi):
                if i < n:
                    lefts.append(i)
                elif i > n:
                    rights.append(i)
            
            right, left = [], []
            for l in lefts:
                if l not in visited:
                    left.extend(backtrack(l, n, mini))
            for r in rights:
                if r not in visited:
                    right.extend(backtrack(r, maxi, n))
            visited.remove(n)
   
            if not right and not left:
                return [TreeNode(n)]
                
            if not right:
                return [TreeNode(n, i) for i in left]
            if not left:
                return [TreeNode(n, None, i) for i in right]
            res.extend([TreeNode(n, i, j) for i in left for j in right])
            return res
        
        ans = []
        for i in range(1,  n + 1):
            visited = set()
            ans.extend(backtrack(i, n + 1, 1))
        
        return ans
            
                    
                    
        