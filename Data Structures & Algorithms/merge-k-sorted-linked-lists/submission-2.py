# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        min_heap = []
        counter = 0

        # only append the head of each list
        for head in lists:
            if head is not None:
                counter +=1
                heapq.heappush(min_heap, (head.val, counter, head))
        
        dummy = ListNode()
        tail = dummy
        
        while min_heap:
            _, _, smallest_node = heapq.heappop(min_heap)

            next_node = smallest_node.next
            if next_node is not None:
                counter += 1
                heapq.heappush(
                    min_heap, (next_node.val, counter, next_node)
                )

            tail.next = smallest_node
            tail = smallest_node

        return dummy.next

        