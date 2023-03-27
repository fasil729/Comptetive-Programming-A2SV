# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = [[root.val]]
        while q:
            arr = []
            temp = []
            while q:
                curr = q.popleft()
                if curr.left:
                    arr.append(curr.left.val)
                    temp.append(curr.left)
                if curr.right:
                    arr.append(curr.right.val)
                    temp.append(curr.right)
            if arr:
                res.append(arr)
            q = deque(temp)
        return reversed(res)
            