# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode(0)
        heap = []
        i = 0
        for node in lists:
            
            while node:
                i += 1
                heap.append([node.val, i, node])
                node = node.next
        
        heapq.heapify(heap)
        curr = root
        while heap:
            curr.next = heapq.heappop(heap)[2]
            curr = curr.next
        return root.next
            
            
            
                
                
                
            
        
        
        