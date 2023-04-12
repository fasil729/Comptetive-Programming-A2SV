class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        def helper(start, end):
            mid = start + (end - start) // 2
            if start == end:
                return nums[start]
            left = helper(start, mid)
            right = helper(mid + 1, end )
            count = 0
            if left == right:
                return left
            else:
                right_count = 0
                left_count = 0
                for num in nums[start:end + 1]:
                    if num == left:
                        left_count += 1
                    elif num == right:
                        right_count += 1
                if left_count > right_count:
                    return left
                return right
        return helper(0, len(nums) - 1)
                
                        
        