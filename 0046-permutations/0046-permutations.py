class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        dictionary = Counter(nums)
        result = []
        
        def backtrack(dictionary, arr):
            if len(arr) == len(nums):
                result.append(arr.copy())
            
            for k in dictionary:
                if dictionary[k] != 0:
                    dictionary[k] -= 1
                    arr.append(k)
                    backtrack(dictionary, arr)
                    arr.pop()
                    dictionary[k] += 1
        backtrack(dictionary, [])
        return result
                
            
            
                    