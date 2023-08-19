class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        
        def binary_search(num, arr):
            left, right = 0, len(arr) - 1
            
            while left < right - 1:
                mid = (left + right) // 2
                if arr[mid] == num:
                    return 0
                elif arr[mid] < num:
                    left = mid
                else:
                    right = mid
            return min(abs(arr[left] - num), abs(arr[right] - num))
               
        
        
        visited = []
        mini = float("inf")
        for i in range(x, len(nums)):
            bisect.insort(visited, nums[i - x])
            num = nums[i]
            res = binary_search(num, visited)
            mini = min(mini, res)
        return mini
        