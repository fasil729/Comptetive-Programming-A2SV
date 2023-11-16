class Solution:
    def findDifferentBinaryString2(self, nums: List[str]) -> str:
        ba
        n = len(nums)
        nums = set(nums)
        def backtrack(binStr):
            
            if len(binStr) == n:
                return binStr not in nums, binStr
            
            isUnique, ans = backtrack(binStr + "0")
            if isUnique:
                return isUnique, ans
            return backtrack(binStr + "1")
        
        return backtrack("")[1]
    
    
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        base_ten = [int(b, 2) for b in nums]
        print(base_ten)
        base_ten = set(base_ten)
        for i in range(n):
            if i not in base_ten:
                binStr = bin(i)[2:]
                return "0" * (n - len(binStr)) + binStr
            
        binStr = bin(n)[2:]
        return "0" * (n - len(binStr)) +  binStr 
            
                
            
        