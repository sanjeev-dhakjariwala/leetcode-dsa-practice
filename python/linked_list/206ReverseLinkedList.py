from typing import *
from linked_list.ListNode import ListNode, create_linked_list_from_string


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp


input_string = "1,2,3,4,5"
head = create_linked_list_from_string(input_string)
rev = Solution().reverseList(head)
current = rev
while current:
    print(current.val, end=" -> ")
    current = current.next
