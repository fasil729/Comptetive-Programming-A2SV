# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        def reverse(head, steps):
            count = 0
            curr = head
            prev = None
            while count < steps:
                curr_next = curr.next
                curr.next = prev
                prev = curr
                curr = curr_next
                count += 1

        prev_left, left_node, right_node = None, None, None
        curr = head
        for index in range(1, right + 1):
            if index == left - 1:
                prev_left = curr
            if index == left:
                left_node = curr
            if index == right:
                right_node = curr
            curr = curr.next

        next_right = right_node.next
        reverse(left_node, right - left + 1)
        left_node.next = next_right

        if prev_left:
            prev_left.next = right_node
            return head
        else:
            return right_node
        