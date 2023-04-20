class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = inf
        arr = [0] * k
        n = len(cookies)
        
        
        def combination(start, maxi):
            nonlocal res
            if start == n:
                res = min(res, maxi)
                return
            if maxi >= res:
                return
            init = maxi
            
            for i in range(k):
                arr[i] += cookies[start]
                maxi = max(arr[i], maxi)
                combination(start + 1, maxi)
                arr[i] -= cookies[start]
                maxi = init
        combination(0, 0)
        return res
        
            
            
            
            
            
            
            
            
            
            # print(arr)
            # nonlocal res
            # tot = 0
            # for i in arr:
            #     tot += cookies[i]
            # diff = sum(cookies) - tot
            # temp = diff / (k - 1)
            # maxi = 0
            # for j in range(n):
            #     if j not in arr:
            #         maxi = max(cookies[j], maxi)
            # if temp <= tot and temp >= maxi:
            #     res = min(res, tot)
            # else:
            #     res = min(res, maxi)
            # if start == n:
            #     return
            # for ind in range(start, n):
            #     arr.add(ind)
            #     combination(ind + 1)
            #     arr.remove(ind)
        
        # # for i in range(0, n):
        # combination(0)
        # return res
                
            
            
        
        