# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        currNum = float("inf")
        currStreak = 0
        maxStreak = 0
        
        def inorder(root):
            nonlocal currStreak
            nonlocal maxStreak
            nonlocal currNum
            nonlocal ans
            if not root:
                return
            inorder(root.left)
            if root.val == currNum:
                currStreak += 1
            else:
                currStreak = 1
                currNum = root.val
            if currStreak == maxStreak:
                ans.append(root.val)
            elif currStreak > maxStreak:
                maxStreak = currStreak
                ans = [root.val]
            inorder(root.right)
           
        inorder(root)
        return ans
                
            
        