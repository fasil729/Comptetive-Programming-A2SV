# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        # brute force approach
        visited = set()
        curr = head
        while curr and curr not in visited:
            visited.add(curr)
            curr = curr.next
            
        if curr:
            return True
        return False
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while fast:
            if fast == slow or fast.next == slow:
                return True
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return False
        