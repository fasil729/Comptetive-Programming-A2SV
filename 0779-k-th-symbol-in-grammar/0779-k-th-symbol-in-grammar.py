class Solution:
    def kthGrammar(self, n: int, k: int) -> int:   # n = 4  k = 5   
        if k == 1:   
            return 0
        change = 0
        while k > 2:  # 5 > 2 true k = 1
            leng = len(bin(k - 1)) - 3 # leng = len(bin(4)) - 2 = 2
            k -= 2 ** leng       # k = k - 2 ** 2  
            change += 1      # change = 1
        k -= 1   # 0
        if change % 2 != 0:
            return 1 - k   # 1
        return k
        
        