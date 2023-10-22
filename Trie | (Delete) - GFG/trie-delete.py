#User function Template for python3

class Solution():
    def deleteKey(self, root, key, depth=0, index=0):
        #your code goes here
        if not root:
            return None
        if len(key) == depth:
            root.isEndOfWord = False
            if isEmpty(root):
                del root
                root = None
            return root
        ind = ord(key[index]) - ord("a")
        root.children[ind] = self.deleteKey(root.children[ind], key, depth + 1, index + 1)
        if isEmpty(root):
            del root
            root = None
        return root
        

def isEmpty(root):
    if not root:
        return True
    for child in root.children:
        if child != None:
            return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        
#use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch)-ord('a')


#Function to insert string into TRIE.    
def insert(root,key):
    
    #if not present, we insert key into trie. If the key is prefix 
    #of trie node, we just mark the leaf node.
    for e in key:
        idx=charToIndex(e)
        
        if not root.children[idx]:
            root.children[idx]=TrieNode()
        
        root=root.children[idx]
    
    #marking last node as leaf.    
    root.isEndOfWord=True

#Function to use TRIE data structure and search the given string.
def search(root, key):
    
    for e in key:
        idx=charToIndex(e)
        
        if not root.children[idx]:
            return
        
        root=root.children[idx]
    
    #returning true if key is present else false.
    return root.isEndOfWord

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        key=input()
        
        t=Trie()
        
        for s in arr:
            insert(t.root,s)
        
        Solution().deleteKey(t.root, key)

        if search(t.root, key):
            print(0)
        else:
            print(1)
# } Driver Code Ends