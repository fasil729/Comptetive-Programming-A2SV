class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        ind = 0
        n = len(ratings)
        visited = {}
        while ind < n - 1:
            if ratings[ind] < ratings[ind + 1]:
                count = 1
                visited[ind] = count
                while ind < n - 1 and ratings[ind] < ratings[ind + 1]:
                    ind += 1
                    count += 1
                    visited[ind] = count
            else:
                visited[ind] = 1
            ind += 1
        ind = n - 1   
        while ind > 0:
            if ratings[ind] < ratings[ind - 1]:
                count = 1
                if ind not in visited:
                    visited[ind] = count
                while ind > 0 and ratings[ind] < ratings[ind - 1]:
                    ind -= 1
                    count += 1
                    if ind in visited:
                        visited[ind] = max(count, visited[ind])
                    else:
                        visited[ind] = count
            else:
                if ind not in visited:
                    visited[ind] = 1
            ind -= 1
        ans = 0
        for v in visited.values():
            ans += v
        return ans
        