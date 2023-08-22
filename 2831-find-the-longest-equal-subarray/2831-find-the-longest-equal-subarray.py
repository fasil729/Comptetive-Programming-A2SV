class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        hash_table = defaultdict(list)
        
        for ind in range(len(nums)):
            hash_table[nums[ind]].append(ind)
            
        maxi = 1
        for num, arr in hash_table.items():
            maxi = max(maxi, self.get_max(arr, k))
        
        return maxi
            
    
    def get_max(self, arr, k):
        start, end = 0, len(arr)
        n = len(arr)
        tot = 0
        maxi = 1
        res = 1
        for end in range(1, n):
            tot += arr[end] - arr[end - 1] - 1
            while tot > k:
                tot -= arr[start + 1] - arr[start] - 1
                res -= 1
                start += 1
            res += 1
            maxi = max(maxi, res)
        return maxi
            
            
        
        