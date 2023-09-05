"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hash_table = {}
        curr = head
        while curr:
            hash_table[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            nex = curr.next
            rand = curr.random
            node = hash_table[curr]
            if nex:
                node.next = hash_table[nex]
            if rand:
                node.random = hash_table[rand]
            curr = curr.next
        
        return hash_table[head]
        