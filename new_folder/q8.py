class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def convert_to_sum_tree(root):
   
    if root is None:
        return 0

   
    left_sum = convert_to_sum_tree(root.left)
    right_sum = convert_to_sum_tree(root.right)
    
   
    old_value = root.data
    
    
    root.data = left_sum + right_sum
    
    
    return old_value + root.data

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)

print("Original Tree (Inorder): ")
inorder_traversal(root)
print('\n')

convert_to_sum_tree(root)

print("\nSum Tree (Inorder): ")
inorder_traversal(root)
