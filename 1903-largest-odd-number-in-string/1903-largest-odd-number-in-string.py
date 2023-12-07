class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        last_ind = 0
        n = len(num)
        
        for ind in range(n - 1, -1, -1):
            if int(num[ind]) % 2:
                last_ind = ind + 1
                break
                
        return num[0:last_ind]
        