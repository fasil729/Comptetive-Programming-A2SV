class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        prev = 0
        
        for num in target:   
            diff = num - prev - 1   
            for i in range(diff):  
                ans.append("Push")
            for i in range(diff):   
                ans.append("Pop")
            ans.append("Push")   
            prev = num
        
        return ans
            
        