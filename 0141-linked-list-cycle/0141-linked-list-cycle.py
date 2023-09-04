# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        while curr and curr not in visited:
            visited.add(curr)
            curr = curr.next
            
        if curr:
            return True
        return False
        # print(pos[0])
        # if pos == -1:
        #     return False
        # return True
        