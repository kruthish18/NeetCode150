# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultNode = ListNode()
        curr = resultNode

        while list1 and list2:

            l1 = list1.val
            l2 = list2.val

            if l1<=l2:
                curr.next = l1
                l1=list1.next
            else:
                curr.next = l2
                l2=list2.next   

            curr = curr.next

        while list1:
            curr.next = list1.val
            list1=list1.next
            curr = curr.next

        while list2:
            curr.next = list2.val
            list2=list2.next
            curr = curr.next

        return resultNode.next