# class Solution:
#     def isAdditiveNumber(self, num: str) -> bool:
#         n = len(num)
#         arr = []
#         def helper(ind, prev):
#             # print(arr)
#             # print(prev)
#             # if prev and prev[0] == "0":
#             #     return False
#             if ind == n and len(arr) > 2 and not prev:
#                 return True
            
            
#             for i in range(ind, n):
#                 to_pop = True
#                 prev += num[i]
                
#                 if len(arr) > 1:
#                     first = int(arr[-2])
#                     second = int(arr[-1])
#                     curr = str(first + second)
#                     if str(first) != arr[-2] or str(second) != arr[-1]:
#                         return False
#                     if curr == prev:
#                         arr.append(curr[:])
#                         new = ""
#                     elif len(curr) < len(prev):
#                         return False
#                     else:
#                         new = prev
#                         to_pop = False
                        
#                 else:
#                     arr.append(prev)
#                     new = ""
#                 if helper(i + 1, new):
#                     return True
#                 if to_pop:
#                     arr.pop()
#             return False
#         return helper(0, "")
class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                if self.is_valid_additive_sequence(0, i, j,num,n):
                    return True
    def is_valid_additive_sequence(self, i, j, k,num,n):
        numa = num[i:j]
        numb = num[j:k]
        num1 = int(num[i:j])
        num2 = int(num[j:k])
        if (len(numa) > 1 and numa[0] == '0') or (len(numb) > 1 and numb[0]=='0'):
            return False

        k_start = k
        while k < n :
            num3 = num1 + num2
            num3_str = str(num3)

            if not num.startswith(num3_str, k):
                return False
            k += len(num3_str)

            num1, num2 = num2, num3

        return True
                    
                
                
        