from ListNode import *
from typing import *


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = None
        tail = dummy
        temp = head

        while temp:
            if temp.val != val:
                tail.next = temp
                tail = tail.next
            temp = temp.next

        return dummy.next


sol = Solution()
head = create_linked_list_from_string("1,2,6,3,4,5,6")
print(sol.removeElements(head, 6))
