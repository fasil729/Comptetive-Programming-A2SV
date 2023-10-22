class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        left, right = k - 1, k + 1
        n = len(nums)
        mini = nums[k]
        ans = nums[k]
        while left >= 0 or right < n:
            if left < 0:
                mini = min(mini, nums[right])
                ans = max(ans, mini * (right - left))
                right += 1
            elif right >= n:
                mini = min(mini, nums[left])
                ans = max(ans, mini * (right - left))
                left -= 1
            else:
                if nums[right] > nums[left]:
                    mini = min(mini, nums[right])
                    ans = max(ans, mini * (right - left))
                    right += 1
                else:
                    mini = min(mini, nums[left])
                    ans = max(ans, mini * (right - left))
                    left -= 1
        return ans
            
        