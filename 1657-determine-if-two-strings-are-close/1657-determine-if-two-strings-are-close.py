class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """

        NOTES:

        1 ->  Swap any two existing characters
        2 ->  Transform every occurrence of one existing character into another existing character, and do the same with the other character   
            E.G "AAB" -> "BBA"

        criteria to be close:

        1 ->  we don't need to bother about the ordering of characters
        2 -> the unique characters set of both strings needs to be equal
        3 ->  the frequency set of both strings needs to be equal

        """
        
        count_1 = Counter(word1)
        count_2 = Counter(word2)
        
        # criteria one fails
        if sorted(count_1.keys()) != sorted(count_2.keys()):
            return False
        
        # criteria two fails
        if sorted(count_1.values()) != sorted(count_2.values()):
            return False
        
        return True
            
        
        
        
        


        