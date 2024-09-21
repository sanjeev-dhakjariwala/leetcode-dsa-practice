from TreeNode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        self.serialize = ""
        def helper(root):
            if not root:
                self.serialize += "null,"
                return
            self.serialize += str(root.val) + ","
            helper(root.left)
            helper(root.right)

        helper(root)
        print(self.serialize)
        return self.serialize
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        arr = data[0: len(data) - 1].split(",")
        print(arr)
        self.i = 0
        def helper():
            if arr[self.i] == 'null':
                self.i += 1
                return None
            node = TreeNode(arr[self.i])
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node

        return helper()


sol = Codec()
root = deserialize("1,2,3,null,null,4,5")
serialize = sol.serialize(root)
sol.deserialize(serialize)
