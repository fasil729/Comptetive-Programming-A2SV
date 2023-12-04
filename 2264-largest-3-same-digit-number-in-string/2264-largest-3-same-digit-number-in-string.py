class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = ""
        n = len(num)
        temp = ""
        
        for ind in range(n):
            if ind == 0 or num[ind] == num[ind - 1]:
                temp += num[ind]
            
            else:
                temp = num[ind]
            
            if len(temp) == 3:
                ans = max(ans, temp)
                temp = ""
        return ans
            
                
                
        