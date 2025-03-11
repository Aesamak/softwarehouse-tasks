class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTreeToDLL:
    def __init__(self):
        self.prev = None  
        self.head = None 

    def convert_to_dll(self, root):
       
        if root is None:
            return
        
       
        self.convert_to_dll(root.left)
        
        
        if self.prev is None:
            self.head = root  
        else:
            root.left = self.prev  
            self.prev.right = root 
        
        self.prev = root  
        
        
        self.convert_to_dll(root.right)

    def print_dll(self):
        
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.right else "")
            current = current.right
        print()

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(15)
root.right.right = Node(25)

bt_to_dll = BinaryTreeToDLL()
bt_to_dll.convert_to_dll(root)
print("Doubly Linked List (Inorder Traversal):")
bt_to_dll.print_dll()
