class Solution:
    def majorityElement1(self, nums: List[int]) -> List[int]:
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
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        candidate1, candidate2, count1, count2 = 0, 1, 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [num for num in (candidate1, candidate2) if nums.count(num) > len(nums) // 3]