class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        visited = set()
        tot = n * (n + 1) // 2

        
        for num in nums:
            if num in visited:
                uni = num
            visited.add(num)
            tot -= num
            
        
            
        
        return [uni, tot + uni]
            
        