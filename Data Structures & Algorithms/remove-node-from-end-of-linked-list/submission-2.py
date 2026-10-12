# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        back = dummy
        front = dummy

        for i in range(n):
            front = front.next

        while front.next:
            back = back.next
            front = front.next
        
        node_to_remove = back.next
        back.next = node_to_remove.next
        node_to_remove.next = None

        return dummy.next
        