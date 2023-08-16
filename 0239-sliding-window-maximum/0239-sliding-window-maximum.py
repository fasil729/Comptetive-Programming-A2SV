class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        start, end = 0, -1
        for num in nums:
            end += 1
            while queue and queue[-1] < num:
                queue.pop()
            queue.append(num)
            if (end - start) + 1 == k:
                ans.append(queue[0])
                if nums[start] == queue[0]:
                    queue.popleft()
                start += 1
        return ans
                
            