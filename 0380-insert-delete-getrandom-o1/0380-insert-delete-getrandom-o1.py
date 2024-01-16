class RandomizedSet:

    def __init__(self):
        """
        NOTES:
            
            -> Initializes the RandomizedSet
            -> each function should works in average O(1) time complexity.
            
            i can start with empty list which is constant time comp
        """
        self.indices = {}
        self.arr = []
        
        

    def insert(self, val: int) -> bool:
        """
        NOTES: 
            ->  Inserts an item val into the set if not present.
            Returns true if the item was not present, false otherwise.
        
        check for prescence in the set -> constant
        add if not present     -> constant
        
        
            
        """
        if val not in self.indices:
            self.indices[val] = len(self.arr)
            self.arr.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        """
            -> Removes an item val from the set if present. Returns true if the                 item was present, false otherwise.
            e.g [3, 4, 2, 1]  val=3
        """
        if val in self.indices:
            ind = self.indices[val]
            
            # swap val to end
            self.arr[ind] = self.arr[-1]
            
            # update the last val indice
            self.indices[self.arr[-1]] = ind
            
            # delete val
            self.arr.pop()
            del self.indices[val]
            
            return True
        
        return False
            
            
        

    def getRandom(self) -> int:
        """
             -> Returns a random element from the current set of elements (it's                -> guaranteed that at least one element exists when this method is called). 
             -> Each element must have the same probability of being returned.
        """
        
        return random.choice(self.arr)
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()