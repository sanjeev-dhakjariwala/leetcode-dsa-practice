from typing import *
from ListNode import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        while k > 0:
            temp = head
            prev = None
            while temp.next != None:
                prev = temp
                temp = temp.next
            if prev:
                prev.next = None
            if temp != head:
                temp.next = head
                head = temp
            k -= 1
        return head


head = create_linked_list_from_string("1,2,3")
sol = Solution()
head = sol.rotateRight(head, 20)
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
