# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from ListNode import *
from typing import *


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
            print(lists)
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

        """ # Define a priority queue
        heap = []

        # Push the first element of each list into the heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        # Dummy node to simplify the code
        dummy = ListNode()
        current = dummy

        print(heap)
        while heap:
            # Pop the smallest element from the heap
            val, i, node = heapq.heappop(heap)

            # Append the popped node to the result
            current.next = node
            current = current.next

            # Move to the next node in the list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next """


head1 = create_linked_list_from_string("1,4,5")
head2 = create_linked_list_from_string("1,3,4")
head3 = create_linked_list_from_string("2,6")
sol = Solution()
print(sol.mergeKLists([head1, head2, head3]))
