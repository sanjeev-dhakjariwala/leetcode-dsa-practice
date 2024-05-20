from typing import *
from ListNode import *

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Function to split the linked list into two halves
        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        # Function to merge two sorted linked lists
        def merge(l1, l2):
            dummy = ListNode()
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 if l1 else l2
            return dummy.next

        # Split the linked list into two halves
        left, right = split(head)

        # Recursively sort each half
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge the sorted halves
        return merge(left, right)

sol = Solution()
head = create_linked_list_from_string("4,2,1,3")
new_head = sol.sortList(head)
# Printing the linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next