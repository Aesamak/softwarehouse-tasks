class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root, nodes):
    if root is None:
        return
    inorder_traversal(root.left, nodes)
    nodes.append(root.data)
    inorder_traversal(root.right, nodes)

def sorted_array_to_bst(start, end, nodes):
    if start > end:
        return None

    mid = (start + end) // 2
    root = Node(nodes[mid])

    root.left = sorted_array_to_bst(start, mid - 1, nodes)
    root.right = sorted_array_to_bst(mid + 1, end, nodes)

    return root

def balance_bst(root):
    nodes = []
    inorder_traversal(root, nodes)  # Get sorted elements
    return sorted_array_to_bst(0, len(nodes) - 1, nodes)

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data, end=" ")
        print_inorder(root.right)

root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.right = Node(15)
root.right.right = Node(20)
root.right.right.right = Node(25)

print("Original BST (Inorder):")
print_inorder(root)

# Balance the BST
balanced_root = balance_bst(root)

print("\nBalanced BST (Inorder):")
print_inorder(balanced_root)
