class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        n = len(arr) / 4
        
        
        for ind in range(len(arr)):
            if ind != 0 and arr[ind] == arr[ind - 1]:
                count += 1
            else:
                count = 1
            
            if count > n:
                return arr[ind]
            
        
        