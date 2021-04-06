""" Create a Bus child class that inherits from the Vehicle class.
 The default fare charge of any vehicle is seating capacity * 100.
  If Vehicle is Bus instance, we need to add an extra 10% on full fare as 
  a maintenance charge. So total fare for bus instance will
   become the final amount = total fare + 10% of the total fare.
Note: The bus seating capacity is 50. so the final fare amount 
should be 5500. You need to override the fare() method of a Vehicle 
class in Bus class."""
class vehicle:
    def __init__(self,seat_capacity,no_of_wheels):
        self.seat_capacity=seat_capacity
        self.no_of_wheels=no_of_wheels
    def default_fare(self):
        return self.seat_capacity*100
    def vehicle_type(self):
        print(f"vehicle is {self.no_of_wheels} wheeler")
    def get_seat_capacity(self):
        return self.seat_capacity
    def get_no_of_wheels(self):
        return self.no_of_wheels

class Bus(vehicle):
    def __init__(self,seat_capacity,no_of_wheels):
        super().__init__(seat_capacity,no_of_wheels)
    def default_fare(self):
        fare = super().default_fare()
        return (fare+((fare*10)//100))
    def __str__(self):
        return f"{self.__class__.__name__} is a vehicle with {super().get_seat_capacity()} seats and {super().get_no_of_wheels()} wheels"
    def __repr__(self):
        return f"{self.__class__.__name__}({super().get_seat_capacity()},{super().get_no_of_wheels()})"
b=Bus(50,4)
print(b.default_fare())
b.vehicle_type()
print(b)
print(repr(b))

