class Solution:
    def minOperations(self, nums: List[int]) -> int:
            # sort the array
            nums.sort()
            duplicate = set()
            n = len(nums)
            
            # remove duplicate numbers
            new_num = []
            for num in nums:
                if num in duplicate:
                    continue
                duplicate.add(num)
                new_num.append(num)
                
            # binary search    
            def binary_search(l, r, target):
                
                while l <= r:
                    mid = (l + r) // 2
                    if new_num[mid] <= target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return l
            
            # compute binary search on every index
            m = len(new_num) - 1
            ans = n - 1
            for i in range(m + 1):
                right = binary_search(i, m, new_num[i] + n - 1)
                ans = min(ans, n - (right - i))
            return ans
                
                