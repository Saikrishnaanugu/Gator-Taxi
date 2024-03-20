from RBTNode import RBTNode
class RedBlackTree:#This is the constructor for the Red-Black Tree class
    def __init__(self):
        self.null_node = RBTNode(None, None)#It initializes the null node and sets the root to the null node.
        #The null node is used to represent empty nodes in the tree, and it is colored black to satisfy the Red-Black Tree properties.
        self.null_node.left = None
        self.null_node.right = None
        self.null_node.color = 0
        self.root = self.null_node

   
    def get_ride(self, key):# To retrieve the ride with the rideNumber equal to the key
        #This method searches the tree for a node with a rideNumber equal to the input key
        temp = self.root #It starts at the root and iteratively moves down the tree towards the appropriate child node based on the value of the current node's rideNumber.

        
        while temp != self.null_node: # Iterating through the tree to find the node with rideNumber equal to the key
            
            if temp.ride.rideNumber == key:#If the current node's rideNumber is equal to the key, the method returns the node.
                return temp
           
            if temp.ride.rideNumber < key:
                temp = temp.right
            else:
                temp = temp.left

        return None #If the method reaches a null node, it means the key is not present in the tree, and the method returns None.

   
    def balance_tree_after_delete(self, node): # Balancing the tree after deletion

        #This section handles the case where the node is the right child of its parent. If the sibling of the parent is red, then the parent and sibling's colors are swapped and the parent is rotated right. 
        #This sets up the sibling to be black and a left child. The parent_sibling variable is updated to reflect the new left child of the parent.
        while node != self.root and node.color == 0:
            if node == node.parent.right:
                parent_sibling = node.parent.left
                if parent_sibling.color != 0:
                    node.parent.color = 1
                    parent_sibling.color = 0
                    self.r_rotation(node.parent)
                    parent_sibling = node.parent.left
                #This section handles the case where the parent's sibling is black and both of its children are also black. In this case, the sibling's color is changed to red and the node is moved up to its parent. However, if the sibling's left child is red, it indicates that a left-right rotation is necessary to balance the tree. This is achieved by rotating the sibling left, then updating the parent_sibling variable to be the new left child of the parent. The colors of parent_sibling, 
                #the parent, and the sibling's right child are then updated, and a right rotation is performed on the parent to balance the tree.
                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    node = node.parent
                else:
                    if parent_sibling.left.color != 1:
                        parent_sibling.right.color = 0
                        parent_sibling.color = 1
                        self.l_rotation(parent_sibling)
                        parent_sibling = node.parent.left

                    parent_sibling.color = node.parent.color
                    node.parent.color = 0
                    parent_sibling.left.color = 0
                    self.r_rotation(node.parent)
                    node = self.root
            #This section handles the case where the node is the left child of its parent. If the sibling of the parent is red, then the parent and sibling's colors are swapped and the parent is rotated left. 
            #This sets up the sibling to be black and a right child. The parent_sibling variable is updated to reflect the new right child of the parent.
            else:
                parent_sibling = node.parent.right
                if parent_sibling.color != 0:
                    node.parent.color = 1
                    parent_sibling.color = 0
                    self.l_rotation(node.parent)
                    parent_sibling = node.parent.right

                if parent_sibling.right.color == 0 and parent_sibling.left.color == 0:
                    parent_sibling.color = 1
                    node = node.parent
                else:
                    if parent_sibling.right.color != 1:
                        parent_sibling.left.color = 0
                        parent_sibling.color = 1
                        self.r_rotation(parent_sibling)
                        parent_sibling = node.parent.right

                    parent_sibling.color = node.parent.color
                    node.parent.color = 0
                    parent_sibling.right.color = 0
                    self.l_rotation(node.parent)
                    node = self.root

        node.color = 0
#This method performs a transplant operation on a Red-Black tree, replacing one node with another. 
#The node argument is the node to be replaced, and the child_node argument is the node that will take its place.
    def __rb_transplant(self, node, child_node):
        if node.parent is None:
            self.root = child_node
        elif node == node.parent.right:
            node.parent.right = child_node
        else:
            node.parent.left = child_node
        child_node.parent = node.parent
#This function delete_node_helper is used to delete a node from the red-black tree based on the rideNumber attribute of the node's ride object. 
#The function takes two arguments, node which is the current node and key which is the rideNumber of the ride to be deleted.

    def delete_node_helper(self, node, key):
        delete_node = self.null_node
        # Traverse the tree to find the node to be deleted
        while node != self.null_node:
            if node.ride.rideNumber == key:
                delete_node = node
            if node.ride.rideNumber >= key:
                node = node.left
            else:
                node = node.right
        # If the node to be deleted is not found in the tree, return None
        if delete_node == self.null_node:
            return
        # If the node to be deleted has a left child, set x to the left child;
        # otherwise, set x to the right child
        heap_node = delete_node.min_heap_node
        y = delete_node
        y_original_color = y.color
        if delete_node.left == self.null_node:
            x = delete_node.right
            self.__rb_transplant(delete_node, delete_node.right)
        elif (delete_node.right == self.null_node):
            x = delete_node.left
            self.__rb_transplant(delete_node, delete_node.left)
        else:
            # If the node to be deleted has two children, find its successor y
            y = self.minimum(delete_node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == delete_node:
                x.parent = y
            else:
                 # Replace y with its right child
                self.__rb_transplant(y, y.right)
                y.right = delete_node.right
                y.right.parent = y
            
            # Replace the node to be deleted with y
            self.__rb_transplant(delete_node, y)
            y.left = delete_node.left
            y.left.parent = y
            y.color = delete_node.color
        # If the original color of y was black, balance the tree
        if y_original_color == 0:
            self.balance_tree_after_delete(x)

        return heap_node

    def balance_after_insert(self, curr_node):
        while curr_node.parent.color == 1:
            if curr_node.parent == curr_node.parent.parent.left:
                
                parent_sibling = curr_node.parent.parent.right

                if parent_sibling.color == 0:
                    
                    if curr_node == curr_node.parent.right:
                        curr_node = curr_node.parent
                        self.l_rotation(curr_node)
                    
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    self.r_rotation(curr_node.parent.parent)
                else:
                    
                    parent_sibling.color = 0
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    curr_node = curr_node.parent.parent

            else:
                parent_sibling = curr_node.parent.parent.left
                if parent_sibling.color == 0:
                    
                    if curr_node == curr_node.parent.left:
                        curr_node = curr_node.parent
                        self.r_rotation(curr_node)
                
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    self.l_rotation(curr_node.parent.parent)
                else:
                    
                    parent_sibling.color = 0
                    curr_node.parent.color = 0
                    curr_node.parent.parent.color = 1
                    curr_node = curr_node.parent.parent

            if curr_node == self.root:
                break
        self.root.color = 0

    def find_rides_in_range(self, node, low, high, res):
        # If the node is a null node, return.
        if node == self.null_node:
            return
        # If the lowest value in the range is less than the current node's value,
        # search for the values in the left subtree.
        if low < node.ride.rideNumber:
            self.find_rides_in_range(node.left, low, high, res)
        # If the current node's value is within the range, add it to the result list.
        if low <= node.ride.rideNumber <= high:
            res.append(node.ride)
        # If the highest value in the range is greater than the current node's value,
        # search for the values in the right subtree.
        self.find_rides_in_range(node.right, low, high, res)

    def get_rides_in_range(self, low, high):
        # Initialize an empty result list.
        res = []
         # Call the recursive function to search for rides in the given range.
        self.find_rides_in_range(self.root, low, high, res)
         # Return the resulting list.
        return res

    def minimum(self, node):
        # Find the minimum node in the subtree with the given node as root
        while node.left != self.null_node:
            node = node.left
        # Return the minimum node.
        return node
    # This function performs a left rotation of the given node x in a binary search tree
    def l_rotation(self, x):
        # Store the right child of x as y
        y = x.right
        # Set the left child of y as the right child of x
        x.right = y.left
        # If the left child of y is not null, set its parent to x
        if y.left != self.null_node:
            y.left.parent = x
        #The l_rotation and r_rotation methods are used to perform left and right rotations, respectively, on a node and its child nodes.
                 #  These rotations are used for balancing the tree during insertions and deletions.
        y.parent = x.parent
        
        if x.parent == None:
            self.root = y
       
        elif x == x.parent.left:
            x.parent.left = y
        
        else:
            x.parent.right = y
      
        y.left = x
        x.parent = y
    # This function performs a right rotation of the given node x in a binary search tree
    def r_rotation(self, x):
       
        y = x.left
        # Set the right child of y as the left child of x
        x.left = y.right
        # If the right child of y is not null, set its parent to x
        if y.right != self.null_node:
            y.right.parent = x
        # Set the parent of y as the parent of x
        y.parent = x.parent
        # If x is the root node, set the root to y
        if x.parent == None:
            self.root = y
        # If x is a right child, set the right child of its parent to y
        elif x == x.parent.right:
            x.parent.right = y
        # If x is a left child, set the left child of its parent to y
        else:
            x.parent.left = y
        # Set the right child of y as x and x as the parent of y
        y.right = x
        x.parent = y

    def insert(self, ride, min_heap):#The insert method is used to insert a new node into the RBT. 
        # It first creates a new RBTNode object with the ride and min heap node, sets its color to red, and then traverses the RBT to find the correct place for insertion. 
        #Once inserted, the method calls balance_after_insert to balance the tree if necessary.
        node = RBTNode(ride, min_heap)

        node.parent = None
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1

        insertion_node = None
        temp_node = self.root
# Traverse the tree to find the correct position to insert the new node
        while temp_node != self.null_node:
            insertion_node = temp_node
            if node.ride.rideNumber < temp_node.ride.rideNumber:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right
                  # Set the parent of the new node and update the root if necessary
        node.parent = insertion_node
        if insertion_node is None:
            self.root = node
        elif node.ride.rideNumber > insertion_node.ride.rideNumber:
            insertion_node.right = node
        else:
            insertion_node.left = node
            # If the parent of the new node is None, color the node black and return
        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.balance_after_insert(node)# Balance the tree after insertion to maintain the Red-Black Tree properties

    def delete_node(self, rideNumber):
        # Define a method to delete a node with a given rideNumber
        return self.delete_node_helper(self.root, rideNumber)# Call the helper function with the root of the tree and the given rideNumber
