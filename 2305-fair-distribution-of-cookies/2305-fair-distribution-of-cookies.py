class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = inf
        arr = [0] * k
        n = len(cookies)
        cookies.sort(reverse=True)
        
        
        def combination(start, maxi):
            nonlocal res
            # if maxi > res:
            #     return
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
                
            
            
        
        