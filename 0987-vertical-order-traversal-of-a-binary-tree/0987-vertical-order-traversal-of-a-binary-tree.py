# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __lt__(self, obj):
        return self.val < obj.val
        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        tree = defaultdict(list)
        # def dfs(root, col):
        #     if not root:
        #         return
        #     tree[col].append(root.val)
        #     dfs(root.left, col - 1)
        #     dfs(root.right, col + 1)
        # dfs(root, 0)
        # using bread first search using priority queue
        def bfs(root):
            heap = [(0, root.val, 0, 0, root)]
            heapq.heapify(heap)
            diff = 0  # i use to differtite nodes which has equal row, col and val
            # print(heap)
            while heap:
                diff += 1
                row, val, col, d, curr = heapq.heappop(heap)
                tree[col].append(val)
                if curr.left:
                    heapq.heappush(heap, (row + 1, curr.left.val, col - 1, diff, curr.left))
                if curr.right:
                    heapq.heappush(heap, (row + 1, curr.right.val, col + 1, diff, curr.right))
                # print(heap)
            return
        bfs(root)    
        res = []
        for key in sorted(tree.keys()):
            res.append(tree[key])
        return res
            
            
            
        
        