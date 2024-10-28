class Node:

    def __init__(self, value):
        self.value = value # Value of the node
        self.left = None # Left child (another Node)
        self.right = None # Right child (another Node)
        self.is_root = False

    def set_right(self, node):
        self.right = node
    
    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left
    
    def set_root(self, value):
        self.is_root = value
