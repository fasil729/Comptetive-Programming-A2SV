# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # calculating the length
        leng = 0
        curr = head
        while curr:
            leng += 1
            curr = curr.next
            
        
        ans = []
        div, mod = divmod(leng, k)
        curr = head
        for i in range(k):
            temp = div
            if mod:
                temp += 1
                mod -= 1
            
            count = 1
            ans.append(curr)
            while curr and count < temp:
                curr = curr.next
                count += 1
            # disconnect the lists
            if curr:
                nex = curr.next
                curr.next = None
                curr = nex
            
        return ans
            
        