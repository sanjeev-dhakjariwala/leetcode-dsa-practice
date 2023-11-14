# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import *
from linked_list.ListNode import *

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2
        return dummy.next


list1 = create_linked_list_from_string("1,2,4")
list2 = create_linked_list_from_string("1,3,4")
sol = Solution()
current = sol.mergeTwoLists(list1, list2)
while current:
    print(current.val, end=" -> ")
    current = current.next