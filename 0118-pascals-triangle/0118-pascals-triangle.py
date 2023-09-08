class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows - 1):
            arr = [1]
            for ind in range(1, len(ans[-1])):
                arr.append(ans[-1][ind] + ans[-1][ind - 1])
            arr.append(1)
            ans.append(arr)
        return ans
        