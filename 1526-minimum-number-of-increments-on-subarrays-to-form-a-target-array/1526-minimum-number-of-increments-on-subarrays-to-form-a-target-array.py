class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        inc = 0
        for i in range(len(target)):
            if i == 0:
                inc += target[i]
            else:
                inc += max(target[i]-target[i-1], 0)

        return inc
        