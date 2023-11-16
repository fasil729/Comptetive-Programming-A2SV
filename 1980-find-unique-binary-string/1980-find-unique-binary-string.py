class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
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
                
            
        