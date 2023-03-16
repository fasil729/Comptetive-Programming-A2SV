class Solution(object):
    def __init__ (self):
        
        self.score_1 = 0
        self.score_2 = 0
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def winner(nums, index, score_1, score_2, turn):
            if not nums:
                score = score_1 >= score_2
               
                
                return score
            else:
                if turn:
                    score_1 += nums[index]
                    
                else:
                    score_2 += nums[index]
                nums = nums[1:] if index == 0 else nums[:-1]
                turn = not turn
                if turn:
                    return winner(nums, 0, score_1, score_2, turn) or winner(nums, -1, score_1, score_2, turn)
                else:
                    return winner(nums, 0, score_1, score_2, turn) and winner(nums, -1, score_1, score_2, turn)
        return winner(nums, 0, 0, 0, True) or winner(nums, -1, 0, 0, True)
        