class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        def helper(start, end):
            
            if start == end:
                return nums[start]
            mid = start + (end - start) // 2
            
            left = helper(start, mid)
            right = helper(mid + 1, end)
            # print(start, mid, end)
            # # print(left, right)
            left_sum = -inf
            right_sum = -inf
            temp = 0
            
            ind = mid + 1
            
            while ind <= end:
                temp += nums[ind]
                right_sum = max(right_sum, temp)
                ind += 1
            ind = mid
            temp = 0
            while ind >= start:
                temp += nums[ind]
                left_sum = max(left_sum, temp)
                ind -= 1
            # print(left_sum, right_sum)
            return max(left, right, left_sum + right_sum)
        return helper(0, len(nums) - 1)
            
            
        