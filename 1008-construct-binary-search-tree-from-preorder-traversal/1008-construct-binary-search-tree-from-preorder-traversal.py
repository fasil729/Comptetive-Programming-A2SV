# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        childs = set()
        root = TreeNode(preorder[0])
        node = root
        stack = [node]
        for ind, val in enumerate(preorder[1:]):
            next_node = TreeNode(val)
            if node.val > next_node.val:
                childs.add(next_node)
                node.left = next_node
            stack.append(next_node)
            new_node = next_node
            for i in range(len(stack)):
                
                new_node = stack[i]
                if val > new_node.val:
                    if next_node not in childs:
                        new_node.right = next_node
                    stack.insert(i, next_node)
                    stack.pop()
                    break
            node = next_node
        return root
                    
            