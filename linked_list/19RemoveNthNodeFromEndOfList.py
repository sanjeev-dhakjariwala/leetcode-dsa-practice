from linked_list.ListNode import *
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
input_string = "1,2,3,4,5"
head = create_linked_list_from_string(input_string)
rev = Solution().removeNthFromEnd(head, 2)
current = rev
while current:
    print(current.val, end=" -> ")
    current = current.next