class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        j = 0
        arr = set([0])
        num = 2
        while num <= n:
            arr.add(num)
            num *= 2
        for i in range(1, n + 1):
            if i in arr:
                j = 0
            ans.append(ans[j] + 1)
            j += 1
            
        return ans
            