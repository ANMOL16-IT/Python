class Vehicle:
    def __init__(self, vehicle_id, model, rate):
        self.vehicle_id = vehicle_id
        self.model = model
        self.rate = rate
    def calculate_rent(self, days):
        return self.rate * days
    def __str__(self):
        return f"{self.vehicle_id} - {self.model}"
    def __repr__(self):
        return f"Vehicle({self.vehicle_id}, {self.model})"
    def __del__(self):
        print(f"Vehicle {self.vehicle_id} deleted")
class Car(Vehicle):pass
class Bike(Vehicle):pass
class ElectricScooter(Vehicle):pass
class Rental:
    def __init__(self, vehicle, days):
        self.vehicle = vehicle
        self.days = days
    def __len__(self):
        return self.days
    def __str__(self):
        return (
            f"Vehicle: {self.vehicle}\n"
            f"Rental Days: {self.days}\n"
            f"Total Rent: Rs. {self.vehicle.calculate_rent(self.days)}"
        )
# Taking input
vehicle_type = input("Enter Vehicle Type: ")
vehicle_id = input("Enter Vehicle ID: ")
model = input("Enter Model: ")
rate = float(input("Enter Rental Rate: "))
days = int(input("Enter Number of Days: "))
# Creating vehicle object
if vehicle_type.lower() == "car":
    vehicle = Car(vehicle_id, model, rate)
elif vehicle_type.lower() == "bike":
    vehicle = Bike(vehicle_id, model, rate)
else:
    vehicle = ElectricScooter(vehicle_id, model, rate)
# Creating rental object
rental = Rental(vehicle, days)
# Displaying details
print("\nVehicle Details:")
print(vehicle)
print("\nRental Details:")
print(rental)
print("\nNumber of Rental Days:", len(rental))
print("\nObject Representation:")
print(repr(vehicle))
# Deleting object
del vehicle