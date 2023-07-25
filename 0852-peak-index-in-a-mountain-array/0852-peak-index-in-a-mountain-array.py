class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1] and arr[mid-1] < arr[mid]: return mid
            if arr[mid] > arr[mid + 1]: right = mid - 1
            else: left = mid + 1