from ListNode import *
from typing import *


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        temp = dummy

        trav = head
        i = 1
        while trav:
            if i % 2 == 1:
                node = ListNode(trav.val)
                temp.next = node
                temp = node
            trav = trav.next
            i += 1
        trav = head
        i = 1
        while trav:
            if trav.val % 2 == 0:
                node = ListNode(trav.val)
                temp.next = node
                temp = node
            trav = trav.next
            i += 1
        temp.next = None


sol = Solution()
head = create_linked_list_from_string("1,2,3,4,5")
sol.oddEvenList(head)
