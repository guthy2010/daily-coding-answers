"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    vals = []
    def encode(node):
        vals.append(str(node.val))
        if node.left:
            encode(node.left)
        else:
            vals.append("L")
        if node.right:
            encode(node.right)
        else:
            vals.append("R")
    encode(root)
    return vals

# This method deserializes the string back into the tree
def deserialize(string_list):
    def create_a_tree(sub_list):
        if sub_list[0] == 'R' or sub_list[0] == 'L':
            del sub_list[0]
            return
        parent = Node(sub_list[0])
        del sub_list[0]
        parent.left = create_a_tree(sub_list)
        parent.right = create_a_tree(sub_list)
        return parent

    if len(string_list) != 0:
        root_node = create_a_tree(string_list)
    else:
        print("ERROR - empty string!")
        return 0

    return root_node


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

print(deserialize(serialize(node)).left.left.val)