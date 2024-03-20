class MinHeapNode:
    def __init__(self, ride, rbt, min_heap_index):
        # Constructor for the MinHeapNode class, which represents a node in the min heap
        # that contains a ride object and a reference to the Red-Black tree where the ride is stored.
        # It also stores the index of the node in the min heap.
        self.ride = ride# The ride object stored in the node
        self.rbTree = rbt# The Red-Black tree where the ride is stored
        self.min_heap_index = min_heap_index# The index of the node in the min heap