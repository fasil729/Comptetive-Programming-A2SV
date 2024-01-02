class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)
        ans = []
        distnict = list(set(nums))
        
        while distnict:
            arr = []
            for num in distnict:
                if count[num]:
                    arr.append(num)
                    count[num] -= 1
            
            if arr:
                ans.append(arr)
            distnict = arr
        
        return ans
            
        
        
        