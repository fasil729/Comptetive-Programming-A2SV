class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        n = max(segments, key=lambda x: x[1])[1]
        print(n)
        pref = [0] * n
        end_points = set()
        for s, e, p in segments:
            end_points.add(s)
            end_points.add(e)
            pref[s - 1] += p
            pref[e - 1] -= p
        
        for i in range(1, n):
           
            pref[i] = pref[i] + pref[i - 1]
        ans = []
        end_points = list(end_points)
        end_points.sort()
        # print(end_points)
        for ind in range(len(end_points) - 1):
            start = end_points[ind]
            end = end_points[ind + 1]
            if pref[start - 1] != 0:
                ans.append([start, end, pref[start - 1]])
            
            
        return ans
            
            
        