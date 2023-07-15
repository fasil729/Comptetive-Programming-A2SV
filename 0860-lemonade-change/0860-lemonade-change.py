class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten = 0
        five = 0
        for bill in bills:
           
            if bill == 10:
                ten += 1
                five -= 1
            elif bill == 5:
                five += 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return False
            
                
        return True
        