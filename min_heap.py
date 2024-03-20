from MinHeapnode import MinHeapNode
class MinHeap:
    def __init__(self): #This method initializes the Min Heap instance with an empty list and a current size of 0.
        self.heap_list = [0]
        self.curr_size = 0

    def insert(self, ele): #This method inserts a new element to the Min Heap instance by appending it to the heap list, incrementing the current size, and calling heapify_up to ensure the heap property is maintained.
        self.heap_list.append(ele)
        self.curr_size += 1
        self.heapify_up(self.curr_size)

    def heapify_up(self, p):#This method recursively checks if the parent node of the current node (at index p) has a greater key than the current node.
        # If so, it swaps the two nodes and continues to recursively swap until the heap property is restored
        while (p // 2) > 0:
            if self.heap_list[p].ride.less_than(self.heap_list[p // 2].ride):
                self.swap(p, (p // 2))
            else:
                break
            p = p // 2

    def swap(self, ind1, ind2):#This method swaps the elements at the given indices in the heap list, 
        #and updates their min_heap_index attribute.
        temp = self.heap_list[ind1]
        self.heap_list[ind1] = self.heap_list[ind2]
        self.heap_list[ind2] = temp
        self.heap_list[ind1].min_heap_index = ind1
        self.heap_list[ind2].min_heap_index = ind2

    def heapify_down(self, p): 
        #This method recursively checks if either of the children nodes of the current node (at index p) has a lesser key than the current node. 
        #If so, it swaps the two nodes and continues to recursively swap until the heap property is restored.
        while (p * 2) <= self.curr_size:
            ind = self.get_min_child_index(p)
            if not self.heap_list[p].ride.less_than(self.heap_list[ind].ride):
                self.swap(p, ind)
            p = ind

    def get_min_child_index(self, p):
        if (p * 2) + 1 > self.curr_size:
            return p * 2
        else:
            if self.heap_list[p * 2].ride.less_than(self.heap_list[(p * 2) + 1].ride):
                return p * 2
            else:
                return (p * 2) + 1

    def update_element(self, p, new_key):#This method updates the key of an element at index p by modifying the corresponding tripDuration attribute of the corresponding Ride object. Then, it calls heapify_down or heapify_up to restore the heap property.
        node = self.heap_list[p]
        node.ride.tripDuration = new_key
        if p == 1:
            self.heapify_down(p)
        elif self.heap_list[p // 2].ride.less_than(self.heap_list[p].ride):
            self.heapify_down(p)
        else:
            self.heapify_up(p)

    def delete_element(self, p): #This method deletes the element at index p by swapping it with the last element in the heap list, decrementing the current size, and then calling heapify_down to restore the heap property.

        self.swap(p, self.curr_size)
        # self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapify_down(p)

    def pop(self): #This method returns the root element (i.e. the element with the minimum key) by swapping it with the last element in the heap list, decrementing the current size, and then calling heapify_down to restore the heap property.
        # If the heap is empty, it returns the string "No Rides Available".
        if len(self.heap_list) == 1:
            return 'No Rides Available'

        root = self.heap_list[1]

        self.swap(1, self.curr_size)
        # self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapify_down(1)

        return root



