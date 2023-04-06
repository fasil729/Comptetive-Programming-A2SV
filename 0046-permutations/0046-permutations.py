class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        dictionary = Counter(nums)
        result = []
        
        def backtrack(dictionary, leng, arr):
            if len(arr) == leng:
                result.append(arr.copy())
                
            for key, val in dictionary.items():
                if val > 0:
                    dictionary[key] -= 1
                    arr.append(key)
                    backtrack(dictionary, leng, arr)
                    dictionary[key] += 1
                    arr.pop()
        backtrack(dictionary, len(nums), [])
        return result
                