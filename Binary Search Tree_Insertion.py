class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        #Enter you code here.
        if not self.root:
            self.root = Node(val)
        else:
            node = self.root
            while node:
                if val < node.info:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(val)
                        break
                    
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(val)
                        break
            #node = Node(val)
            
        return self.root
tree = BinarySearchTree()
