class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        def get_index(r, c, k):
            if k < 0:
                 r = max(0, r + k)            
                 c = max(0, c + k)
            else:
                r = min(n, r + k)
                c = min(m, c + k)
            return r, c
            
        pref_mat = [[0] * (m + 1)]
        for row in mat:
            pref = [0]
            for num in row:
                pref.append(pref[-1] + num)
            pref_mat.append(pref)
        for row in range(1, n + 1):
            for col in range(1, m + 1):
                pref_mat[row][col] += pref_mat[row - 1][col]
        ans = [[0] * m for i in range(n)] 
        for row in range(n):
            for col in range(m):
                l_r, l_c = get_index(row, col, -k)
                r_r, r_c = get_index(row + 1, col + 1, k)
                ans[row][col] = pref_mat[r_r][r_c] +  pref_mat[l_r][l_c] - pref_mat[r_r][l_c]- pref_mat[l_r][r_c]
        
        return ans
                
        