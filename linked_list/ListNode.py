class ListNode:
    def __init__(self, x=-1, next=None):
        self.val = x
        self.next = None




def create_linked_list_from_string(input_string):
    # Split the input_string by commas to get individual values
    values = input_string.split(',')

    # Initialize the head of the linked list
    head = ListNode(None)
    current = head

    # Create ListNode instances and link them
    for value in values:
        value = int(value)
        current.next = ListNode(value)
        current = current.next

    # Return the linked list, starting from the actual head (not the initial None value)
    return head.next


# Example usage:
input_string = "3,2,0,-4"
head = create_linked_list_from_string(input_string)

# Printing the linked list
""" current = head
while current:
    print(current.val, end=" -> ")
    current = current.next """
