# class ListNode:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp

        return head        