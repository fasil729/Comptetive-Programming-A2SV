# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        size = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            size += 1
        return size
    
    def solve(self, head, k, size):
        if size < k:
            return head
        if head is None:
            return None
        curr = head
        nn = None
        prev = None
        ct = 0
        while curr is not None and ct < k:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
            ct += 1
        head.next = self.solve(nn, k, size - k)
        return prev
    
    def reverseKGroup(self, head, k):
        n = self.length(head)
        return self.solve(head, k, n)
        