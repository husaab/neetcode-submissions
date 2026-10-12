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

        for node_list in lists:
            node = node_list
            while node:
                counter+=1
                heapq.heappush(min_heap, (node.val, counter, node))
                node = node.next
        
        if not min_heap:
            return

        _, _, start_node = heapq.heappop(min_heap)
        prev = start_node

        while min_heap:
            _, _, curr_node = heapq.heappop(min_heap)
            prev.next = curr_node
            prev = curr_node

        return start_node
        


        