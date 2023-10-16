class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(1, rowIndex + 1):
            ans = [1]
            for i in range(1, i):
                ans.append(prev[i] + prev[i - 1])
            ans.append(1)
            prev = ans
        return prev