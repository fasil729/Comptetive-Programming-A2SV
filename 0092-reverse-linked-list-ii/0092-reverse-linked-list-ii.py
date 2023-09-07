# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        
        dummy = ListNode(0, head)
        
        leftPrev, cur = dummy, head
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
            
        prev = None
        for i in range(right - left + 1):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        leftPrev.next.next, leftPrev.next = cur, prev
        return dummy.next
        
            
        