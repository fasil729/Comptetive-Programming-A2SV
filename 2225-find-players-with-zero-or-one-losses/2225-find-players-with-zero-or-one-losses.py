class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = defaultdict(int)
        losers = defaultdict(int)
        ans = [[], []]
        
        # building dictionaries
        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1
            
        
        # filling ans[0]
        for winner in winners:
            if winner not in losers:
                ans[0].append(winner)
        
        # filling ans[1]
        for loser in losers:
            if losers[loser] == 1:
                ans[1].append(loser)
         
        # sort in increasing order
        ans[0].sort()
        ans[1].sort()
        
        return ans
                
            
            
        
        
        

"""
NOTEs: 

   ->  answer[0] is a list of all players that have not lost any matches.
   ->  answer[1] is a list of all players that have lost exactly one match.
   ->  The values in the two lists should be returned in increasing order.
   ->  I should only consider the players that have played at least one match.
   
       e.g matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
       ans [[1, 2, 10], [4, 5, 7, 8]]
       
       winners = {1:1, 2:1, 3:1, 5:2, 4:3, 10:1}
       
       losers = {3:2, 6:2, 5:1, 8:1, 9:2, 4:1 }
       
       o(n)  time
       o(n)  space
    
"""