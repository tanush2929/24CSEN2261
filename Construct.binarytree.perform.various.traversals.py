# Define a class for a Node in the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Inorder Traversal: Left, Root, Right
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

# Preorder Traversal: Root, Left, Right
def preorder_traversal(node):
    if node:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Postorder Traversal: Left, Right, Root
def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")

# Level Order Traversal (Breadth-First)
def level_order_traversal(root):
    if not root:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Constructing a simple binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Displaying the traversals:
print("Inorder Traversal:")
inorder_traversal(root)
print("\nPreorder Traversal:")
preorder_traversal(root)
print("\nPostorder Traversal:")
postorder_traversal(root)
print("\nLevel Order Traversal:")
level_order_traversal(root)
