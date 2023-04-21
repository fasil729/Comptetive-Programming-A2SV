class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        arr = []
        def helper(ind, prev):
            # print(arr)
            # print(prev)
            # if prev and prev[0] == "0":
            #     return False
            if ind == n and len(arr) > 2 and not prev:
                return True
            
            
            for i in range(ind, n):
                to_pop = True
                prev += num[i]
                
                if len(arr) > 1:
                    first = int(arr[-2])
                    second = int(arr[-1])
                    curr = str(first + second)
                    if str(first) != arr[-2] or str(second) != arr[-1]:
                        return False
                    if curr == prev:
                        arr.append(curr[:])
                        new = ""
                    elif len(curr) < len(prev):
                        return False
                    else:
                        new = prev
                        to_pop = False
                        
                else:
                    arr.append(prev)
                    new = ""
                if helper(i + 1, new):
                    return True
                if to_pop:
                    arr.pop()
            return False
        return helper(0, "")

                    
                
                
        