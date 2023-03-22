class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        [0,2,-1]
        
        [-1, 0, 0, 1]
        
        [-1, -1, -1, 0]
        
        """
        
        arr = [0] * (len(s))
        for start, end, direction in shifts:
            if direction:
                arr[start] += 1
                if end != len(s) - 1:
                    arr[end + 1] -= 1
            else:
                arr[start] -= 1
                if end != len(s) - 1: 
                    arr[end + 1] += 1
        for j in range(1, len(arr)):
            arr[j] += arr[j - 1]
        res = ""   
        for ind, shift in enumerate(arr):
                res += chr(97 + (ord(s[ind]) % 97 + shift) % 26)
        return res
        
        