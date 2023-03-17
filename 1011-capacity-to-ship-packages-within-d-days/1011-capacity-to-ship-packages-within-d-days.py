class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getDays(weights, capacity):
            day = 1
            sum = 0
            for i in weights:
                if sum + i <= capacity:
                    sum += i
                else:
                    day += 1
                    sum = i
            return day
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = low + (high - low) // 2
            if getDays(weights, mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low