# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we have list1 and list2

        # we want to continuously check if list1.val > list2.val:
        # then we say head=list1
        # list1 = list1.next
        # else, head = list2
        # list2=list2.next

        # and we say while list1 or list 2
        if not list2:
            return list1
        if not list1:
            return list2

        if not list1 and list2:
            return None

        head = None

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        curr_node = head

        while list1 or list2:
            if not list1:
                curr_node.next=list2
                break
            if not list2:
                curr_node.next=list1
                break

            if list1.val < list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            
            curr_node = curr_node.next
        
        return head
                

        