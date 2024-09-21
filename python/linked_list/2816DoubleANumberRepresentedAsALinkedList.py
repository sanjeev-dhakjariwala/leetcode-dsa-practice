from typing import *
from ListNode import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            p = head
            q = None
            r = None

            while p:
                r = q
                q = p
                p = p.next
                q.next = r

            return q

        head = reverse(head)
        carry = 0
        dummy = ListNode(-1)
        t = dummy
        while head:
            s = (head.val + head.val + carry)
            carry = s // 10
            n = ListNode(s % 10)
            t.next = n
            t = n
            head = head.next
        if carry:
            n = ListNode(carry)
            t.next = n
            t = n
        return reverse(dummy.next)


sol = Solution()
head = create_linked_list_from_string("9,9,9")
new_head = sol.doubleIt(head)
# Printing the linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
