# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        arr = [node.val] 
        while node.next: 
            node = node.next
            arr.append(node.val)
        def merge_sort(start, end):
            mid = start + (end - start) // 2
            if start == end:
                return [arr[start]]
            left = merge_sort(start, mid)
            right = merge_sort(mid + 1, end)
            res = []
            r = 0
            for l in left:
                while r < len(right) and l > right[r]:
                    res.append(right[r])
                    r += 1
                res.append(l)
            while r < len(right):
                    res.append(right[r])
                    r += 1
            return res
        arr = merge_sort(0, len(arr) - 1)
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
        