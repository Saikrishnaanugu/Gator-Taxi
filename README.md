
## GatorTaxi Ride Management System

# Overview
A new software program designed for the ride-sharing business GatorTaxi to manage ride requests efficiently. The system handles tasks such as printing ride details, adding new ride requests, canceling trips, and modifying trip information. It uses a min-heap and a Red-Black Tree (RBT) to organize and manage ride requests based on ride cost, trip time, and ride number.

# Features
Supports multiple operations including printing ride details, adding new ride requests, canceling rides, and updating trip information.
Prioritizes ride requests based on ride cost and trip duration.
Utilizes a min-heap to efficiently choose the next ride request with the lowest travel cost.
Implements a Red-Black Tree to store ride requests in order of ride number.
Handles up to 2000 active rides simultaneously.

# Environment
Programming Language: Python

# Commands to Run:
make run input_file.txt
python gator_taxi.py

# Structure
The project folder consists of the following files:
Makefile
gator_taxi.py
MinHeapnode.py
RBTNode.py
RBTTree.py
min_heap.py
input_file
output_file

# Usage
Clone the repository to your local machine.
Navigate to the project directory.
Use the provided commands to run the source code.
Follow the input file format to perform various operations on ride requests.

# Operations
print(rideNumber): Print details of a single ride request.
print(rideNumber1, rideNumber2): Print details of multiple ride requests within a range.
insert(rideNumber, rideCost, tripDuration): Add a new ride request.
getNextRide(): Retrieve the next ride request with the lowest travel cost.
cancelRide(rideNumber): Cancel a ride request.
updateTrip(rideNumber, new_tripDuration): Update trip duration for a ride request.

# Implementation
Ride requests are stored in a min-heap and sorted by trip length and ride fee.
A Red-Black Tree (RBT) is used to store ride requests ordered by ride number.
Ride requests are represented by objects with attributes rideNumber, rideCost, and tripDuration.
Additional Functions
balance_tree_after_delete(): Balance the Red-Black Tree after deleting a ride request.
balance_tree_after_insert(): Rebalance the Red-Black Tree after inserting a new ride request.
l_rotation(self,x): Perform a left rotation in the Red-Black Tree.
r_rotation(self, x): Perform a right rotation in the Red-Black Tree.
