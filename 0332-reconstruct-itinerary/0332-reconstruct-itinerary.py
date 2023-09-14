class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airport = defaultdict(list)
        tickets.sort()
        for fro, to in tickets:
            airport[fro].append(to)
            
        ans = ["JFK"]
        def dfs(src):
            if len(ans) == len(tickets) + 1:
                return True
            if src not in airport:
                return False
            
            temp = list(airport[src])
            for i, v in enumerate(temp):
                airport[src].pop(i)
                ans.append(v)
                if dfs(v): return True
                airport[src].insert(i, v)
                ans.pop()
            return False
        dfs("JFK")        
        return ans
