class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxi = 0
        ind = 0
        while ind < len(arr):
            if maxi >= arr[ind]:
                ind += 1
                continue
            maxi += 1
            ind += 1
        return maxi
        