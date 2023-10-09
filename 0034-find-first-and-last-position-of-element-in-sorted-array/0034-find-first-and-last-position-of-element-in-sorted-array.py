class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            # print(l, r)
            mid = (l + r) // 2
            print(l, r, mid)
            if nums[mid] < target:
                l = mid + 1
            else:
                r= mid - 1
        left = l
        l, r = 0, len(nums) - 1
        while l <= r:
            print(l, r)
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        if left == l:
            return [-1, -1]
        return [left, l - 1]
        