class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        n = len(word1)
        m = len(word2)
        
        ind1 = 0
        ind2 = 0
        sub1 = 0
        sub2 = 0
        s1 = word1[0]
        s2 = word2[0]
        
        while ind1< n and ind2 < m:
            s1 = word1[ind1]
            s2 = word2[ind2]
            
            
            if s1[sub1] != s2[sub2]:
                return False
            
            sub1 += 1
            sub2 += 1
            if sub1 >= len(s1):
                sub1 = 0
                ind1 += 1
                
            
            if sub2 >= len(s2):
                ind2 += 1
                sub2 = 0
       
        return ind1 == n and ind2 == m
            
        