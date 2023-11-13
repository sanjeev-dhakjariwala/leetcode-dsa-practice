from typing import *
from linked_list.ListNode import ListNode, create_linked_list_from_string


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        def helper(head):
            if head.next is None:
                return head
            temp = helper(head.next)
            head.next.next = head
            head.next = None
            return temp
        return helper(head)


input_string = "1,2,3,4,5"
head = create_linked_list_from_string(input_string)
rev = Solution().reverseList(head)
current = rev
while current:
    print(current.val, end=" -> ")
    current = current.next
