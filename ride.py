class Ride: # Define a class to represent a ride
# Define the constructor for the class
    def __init__(self, rideNumber, rideCost, tripDuration):
       # Set the rideNumber, rideCost, and tripDuration of the ride
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration

    def less_than(self, other_ride):# Define a method to compare the current ride with another ride
         # Compare the rideCost of the current ride with the other ride
        if self.rideCost < other_ride.rideCost:
            return True
        elif self.rideCost > other_ride.rideCost:
            return False
        elif self.rideCost == other_ride.rideCost: # If the rideCost is the same, compare the tripDuration
            if self.tripDuration > other_ride.tripDuration:
                return False
            else:
                return True
