class Solution:
    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        row_leng = [len(nums[i]) for i in range(n)]
        
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < row_leng[row]
        queue = deque([(0, 0)])
        ans = []
        visited = set()
        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])
            direc = [(1,0), (0, 1)]
            for r, c in direc:
                n_r = row + r
                n_c = col + c
                if inbound(n_r, n_c) and (n_r, n_c) not in visited:
                    visited.add((n_r, n_c))
                    queue.append((n_r, n_c))
        return ans
             
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        arr = []
        for row in range(n):
            col = 0
            for num in nums[row]:
                arr.append((col, row))
                col += 1
        arr.sort(key=lambda x: (x[0] + x[1], x))
        ans = []
        for col, row in arr:
            ans.append(nums[row][col])
        return ans
        