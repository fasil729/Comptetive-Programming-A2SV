class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(nums, target, rightbias):
            low, high = 0, len(nums) - 1
            ind = -1
            while low <= high:
                mid = low + (high - low) // 2
                
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    ind = mid
                    if rightbias:
                        low = mid + 1
                    else:
                        high = mid - 1
            return ind
        left = binary(nums, target, False)
        right = binary(nums, target, True)
        return [left, right]
            