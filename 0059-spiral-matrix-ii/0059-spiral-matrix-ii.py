class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0]*n for _ in range(n)]
        i=0
        start_col,start_row,end_col,end_row=0,0,n,n
        
        while start_col<end_col or start_row<end_row:
            for c in range(start_col,end_col):
                i+=1
                ans[start_row][c]=i

            start_row+=1
            for r in range(start_row,end_row):
                i+=1
                ans[r][end_col-1]=i

            end_col-=1

            for c in range(end_col-1,start_col-1,-1):
                i+=1
                ans[end_row-1][c]=i

            end_row-=1
            for r in range(end_row-1,start_row-1,-1):
                i+=1
                ans[r][start_col]=i

            start_col+=1

        return ans                    
        