class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0:
            return []
        
        nums.sort()
        ans = []
        count = 0
        temp = []
        mini = nums[0]
        n = len(nums)
        
        for ind, num in enumerate(nums):
            if ind == n - 1 and num - mini <= k:
                temp.append(num)
                count += 1
                
            if count == 3:
                ans.append(temp)
                temp = []
                count = 0
                mini = num
                
            if num - mini <= k:
                temp.append(num)
                count += 1
            else:
                return []
            
            
        
        return ans
        