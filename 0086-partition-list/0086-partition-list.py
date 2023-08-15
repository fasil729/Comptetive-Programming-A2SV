# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = curr_left = ListNode()
        right_dummy = curr_right = ListNode()
        curr = head
        
        while curr != None:
            if curr.val >= x:
                curr_right.next = ListNode(curr.val)
                curr_right = curr_right.next
            else:
                curr_left.next = ListNode(curr.val)
                curr_left = curr_left.next
            curr = curr.next
        curr_left.next = right_dummy.next
        return left_dummy.next
            
        