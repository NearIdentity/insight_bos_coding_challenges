"""
Given a binary tree, find its maximum depth
The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node
"""


# Constructor to create a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traverse(tree):
    # works for some cases
    depth = 1
    max_depth = 0
    if tree.left:
        depth += 1
        traverse(tree.left)
    print(tree.data)
    if tree.right:
        depth += 1
        traverse(tree.right)
    if depth > max_depth:
        max_depth = depth
    return(max_depth)


def depth_helper(node):
    max_depth = traverse(node)
    return(max_depth)


#PLEASE DO NOT CHANGE THIS
def find_max_depth(tree):
    depth = depth_helper(tree)
    return depth


#test cases
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print ("Depth of tree is %d, and the expected result is 3" %(find_max_depth(root),))


if __name__ == "__main__":
    main()
