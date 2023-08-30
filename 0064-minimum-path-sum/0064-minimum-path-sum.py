class Solution:
    def minPathSum(self,grid:List[List[int]])->int:
        @lru_cache(None)
        def fn(i,j):
            if i==0 and j==0:
                return grid[i][j]

            if i<0 or j<0:
                return inf

            return grid[i][j]+min(fn(i-1,j),fn(i,j-1))

        return fn(len(grid)-1,len(grid[0])-1)  
        