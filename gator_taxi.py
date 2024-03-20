
import sys
from ride import Ride
from min_heap import MinHeap
from min_heap import MinHeapNode
from RBTTree import RedBlackTree
from RBTNode import RBTNode

def insert_ride(ride, heap, rbt):
   # Check if the rideexists in the RBTTree
    if rbt.get_ride(ride.rideNumber) is not None:
        # If the ride already exists, add an error message to the output file and exit the program
        
        add_to_output(None, "Duplicate RideNumber", False)
        sys.exit(0)
        return
    
    rbt_node = RBTNode(None, None) # Create a new RBTNode object to represent the ride in the Red-Black Tree
    min_heap_node = MinHeapNode(ride, rbt_node, heap.curr_size + 1)
    # Create a new MinHeapNode object to represent the ride in the MinHeap,passing in the ride object, 
    # the RBTNode object,and the current size of the heap
   
    heap.insert(min_heap_node) # Insert the new MinHeapNode object into the MinHeap
    rbt.insert(ride, min_heap_node) 
    # Insert the new ride into the Red-Black Tree, passing in the ride object and the corresponding MinHeapNode object


def add_to_output(ride, message, list): # Open the output file in append mode
    
    file = open("output_file.txt", "a")
    
    if ride is None:# If the ride object is None, write the message to the output file as a new line
        file.write(message + "\n")
    else:# If the ride object is not None, format the ride information and write it to the output file
        message = ""
       # If the 'list' parameter is False, format the ride information as a single tuple and write it to the output file
        if not list: # If the 'list' parameter is False, format the ride information as a single tuple and write it to the output file
            message += ("(" + str(ride.rideNumber) + "," + str(ride.rideCost) + "," + str(ride.tripDuration) + ")\n")
        else:  # If the 'list' parameter is False, format the ride information as a single tuple and write it to the output file
           
            if len(ride) == 0:# If the list is empty, write a tuple of zeroes to the output file
                message += "(0,0,0)\n"
            
            for i in range(len(ride)):
                if i != len(ride) - 1:
                    message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + "),")
                else:
                    message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + ")\n")
        
        file.write(message) # Write the formatted message to the output file
    
    file.close()# Close the output file

def print_ride(rideNumber, rbt):
    # This function prints the details of a single ride with the given ride number.
# If the ride number is not found, it prints a default ride object to the output file.
    res = rbt.get_ride(rideNumber)
    
    if res is None:
        add_to_output(Ride(0, 0, 0), "", False)
    else:
        
        add_to_output(res.ride, "", False)


def print_rides(l, h, rbt):

    # This function prints the details of all rides with a ride number within a given range.
# It retrieves the rides using the RBT get_rides_in_range method and passes the resulting list to the output file.
    list = rbt.get_rides_in_range(l, h)
    add_to_output(list, "", True)



    # This function retrieves the next ride request from the top of the heap and removes the corresponding node from the RBT.
    # It writes the ride details to the output file.
      # If the heap is empty, it prints a message indicating that there are no active ride requests to the output file.
def get_next_ride(heap, rbt):
    if heap.curr_size != 0:
        popped_node = heap.pop()
        rbt.delete_node(popped_node.ride.rideNumber)
        add_to_output(popped_node.ride, "", False)
    
    else:
        add_to_output(None, "No active ride requests", False)


def cancel_ride(ride_number, heap, rbt):# This function cancels a ride request with the given ride number.
# It deletes the corresponding node from the RBT and removes the corresponding heap element using the min_heap_index attribute.
    heap_node = rbt.delete_node(ride_number)
    if heap_node is not None:
        heap.delete_element(heap_node.min_heap_index)


def update_ride(rideNumber, new_duration, heap, rbt):
    # This function updates the trip duration of a ride with the given ride number.
# It retrieves the ride from the RBT and checks the new duration against the current trip duration.
# If the new duration is shorter, it updates the corresponding heap element with the new duration.
# If the new duration is between the current duration and twice the current duration, 
# it cancels the ride and inserts a new ride object with the updated duration and a cost increase of 10.
# If the new duration is longer than twice the current duration, it cancels the ride.
    rbt_node = rbt.get_ride(rideNumber)
    if rbt_node is None:
        print("")
   
    elif new_duration <= rbt_node.ride.tripDuration:
        heap.update_element(rbt_node.min_heap_node.min_heap_index, new_duration)
    
    elif rbt_node.ride.tripDuration < new_duration <= (2 * rbt_node.ride.tripDuration):
        cancel_ride(rbt_node.ride.rideNumber, heap, rbt)
        insert_ride(Ride(rbt_node.ride.rideNumber, rbt_node.ride.rideCost + 10, new_duration), heap, rbt)
    else:
        cancel_ride(rbt_node.ride.rideNumber, heap, rbt)


if __name__ == "__main__": # Check if the script is being run as the main program
    heap = MinHeap()# Create a new instance of a MinHeap
    rbt = RedBlackTree()# Create a new instance of a RedBlackTree
# Open a new file in write mode and then immediately close it
    # This is done to overwrite the file if it already exists

    file = open("output_file.txt", "w")
    file.close()
    file = open(sys.argv[1], "r") # Open the input file specified in the command line arguments
    for s in file.readlines(): # Iterate over each line in the input file
        n = [] # Extract the integers from the parentheses in the line
        for num in s[s.index("(") + 1:s.index(")")].split(","):
            if num != '':
                n.append(int(num))
        if "Insert" in s: # Check what type of command is being executed
             # If it is an insert command, create a new ride object from the extracted integers
            # and then insert it into both the MinHeap and RedBlackTree
            insert_ride(Ride(n[0], n[1], n[2]), heap, rbt)
        elif "Print" in s: # If it is a print command, check how many arguments are provided
            if len(n) == 1:# If only one argument is provided, print the details of the ride with that ID
             
                print_ride(n[0], rbt)
            elif len(n) == 2: # If two arguments are provided, print the details of all rides with IDs between the two arguments
                print_rides(n[0], n[1], rbt)
        elif "UpdateTrip" in s: # If it is an update command, update the trip distance of the ride with the provided ID
            update_ride(n[0], n[1], heap, rbt)
        elif "GetNextRide" in s:# If it is a get next ride command, get the ride with the smallest distance travelled
            get_next_ride(heap, rbt)
        elif "CancelRide" in s: # If it is a cancel ride command, cancel the ride with the provided ID
            cancel_ride(n[0], heap, rbt)

