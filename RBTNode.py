class RBTNode  :# Define a class to represent a node in the Red-Black Tree
       # Define the constructor for the class

    def __init__(self, ride, min_heap_node):
        # Set the ride, parent, left, right, color, and min_heap_node of the node
        self.ride = ride
        self.parent = None  #parent
        self.left = None  
        self.right = None  
        self.color = 1  #colour nodes, red and black
        self.min_heap_node = min_heap_node