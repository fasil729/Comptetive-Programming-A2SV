class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        first, second = None, None
        ind = 1
        while ind < len(arr):
            if arr[ind - 1] == arr[ind]:
                ind += 1
                continue
            if arr[ind - 1] > arr[ind]:
                first = ind - 1
                second = ind
            if first != None and arr[ind] < arr[first]:
                second = ind
            ind += 1
                
        if first != None  and second != None:
            arr[first], arr[second] = arr[second], arr[first]
        return arr