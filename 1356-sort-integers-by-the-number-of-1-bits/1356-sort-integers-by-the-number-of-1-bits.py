class Solution:
    def sortByBits1(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=lambda x: bin(x).count("1"))
        return arr
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        def find_weight(num):
            weight = 0
            
            while num:
                weight += 1
                num &= (num - 1)
            
            return weight
        
        arr.sort(key = lambda num: (find_weight(num), num))
        return arr
        