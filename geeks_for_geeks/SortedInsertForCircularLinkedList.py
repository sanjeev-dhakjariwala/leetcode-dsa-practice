from Node import *


class Solution:
    def sortedInsert(self, head, data):
        # code here
        temp = head

        while temp.next != head:
            node = temp.next
            if data >= temp.val and data <= node.val:
                t = Node(data)
                temp.next = t
                t.next = node
                break
            temp = temp.next

        return head


sol = Solution()
head = create_linked_list_from_string("-15,-9,-6,5,7,14")
temp = head
while temp:
    if temp.next == None:
        temp.next = head
        break
    temp = temp.next
 
ans = sol.sortedInsert(head, -19)
