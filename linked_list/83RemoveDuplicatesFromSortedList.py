from ListNode import *
from typing import *


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy

        while head:
            if head.next:
                if head.val != head.next.val:
                    temp.next = head
                    temp = temp.next
                elif not head.next.next and head.val != head.next.val:
                    temp.next = head.next
            head = head.next
        return dummy.next


sol = Solution()
head = create_linked_list_from_string("1,1,2,3,3")
current = sol.deleteDuplicates(head)
while current:
    print(current.val, end=" -> ")
    current = current.next
