class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(string):
    if string == "null":
        return None

    values = string.split(",")
    root = TreeNode(int(values[0]))
    queue = [root]
    i = 1

    while i < len(values):
        node = queue.pop(0)

        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root


# Example usage
""" input_string1 = "3,4,5,1,2,null,null,null,null,0"
input_string2 = "3,4,5,1,2"
root1 = deserialize(input_string1)
root2 = deserialize(input_string2)
print(root1.val)
print(root2.val) """
# Now you have the binary tree stored in 'root'
