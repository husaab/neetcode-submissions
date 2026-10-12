# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # floyds cycle, and we know floyds cycle grabs us by the end of it, slow = middle
        # fast = end

        # so over here, by the end of this , slow will equal to

        prev = None
        curr_node = slow.next
        slow.next = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev

            prev = curr_node
            curr_node = next_node
        
        right_starting = prev
        left_starting = head

        while right_starting:
            left_next = left_starting.next
            right_next = right_starting.next

            left_starting.next = right_starting
            right_starting.next = left_next

            left_starting = left_next
            right_starting = right_next
