class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        maxi, sec_maxi = (0, 0), (0, 0)
        n = len(nums)
        ind = 0
        while ind < n:
            temp = nums[ind]
            freq = 0
            while ind < n and nums[ind] == temp:
                ind += 1
                freq += 1
            if freq >= maxi[0]:
                sec_maxi = maxi
                maxi = (freq, temp)
            elif freq >= sec_maxi[0]:
                sec_maxi = (freq, temp)
        ans = []
        if maxi[0] > n // 3:
            ans.append(maxi[1])
        if sec_maxi[0] > n // 3:
            ans.append(sec_maxi[1])
        return ans