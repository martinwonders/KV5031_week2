class Vehicle:
    def __init__(self, make, model, license_plate, driver_id="000", mileage=0, location="", seats=4, notes=""):
        self.make = make
        self.model = model
        self.license_plate = license_plate
        self.driver_id = driver_id
        self.mileage = mileage
        self.location = location
        self.seats = seats
        self.notes = notes

    def display_info(self):
        return f"{self.make} {self.model} (License: {self.license_plate})"

    def get_rental_rate(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def __init__(self, make, model, license_plate, driver_id="000", mileage=0, location="", seats=4, notes=""):
        super().__init__(make, model, license_plate, driver_id, mileage, location, seats, notes)

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"

    def get_rental_rate(self):
        return 80

class Truck(Vehicle):
    def __init__(self, make, model, license_plate, driver_id="000", mileage=0, location="",
                 seats=2, notes="", payload=0, bed_length=0, bed_width=0, bed_height=0):
        super().__init__(make, model, license_plate, driver_id, mileage, location, seats, notes)
        self.payload = payload
        self.bed_length = bed_length
        self.bed_width = bed_width
        self.bed_height = bed_height

    def display_info(self):
        return (f"{super().display_info()}, Payload: {self.payload}kg,"
                f"Bed Dimensions: (L:{self.bed_length}, W:{self.bed_width}, H:{self.bed_height})")

    def get_rental_rate(self):
        return 80

class Rental:
    def __init__(self, vehicle, driverID, duration):
        self.vehicle = vehicle
        self.driverID = driverID
        self.duration = duration

    def calculate_cost(self):
        return self.vehicle.get_rental_rate() * self.duration

    def generate_invoice(self):
        return f"Invoice for Driver ID: {self.driverID}\n" \
               f"Vehicle: {self.vehicle.display_info()}\n" \
               f"Duration: {self.duration} day(s)\n" \
               f"Total Cost: £{self.calculate_cost()}"

vehicles = [
    Car("Toyota", "Corolla", "ABC123", location="New York", mileage=10000),
    Truck("Ford", "F-150", "XYZ789", payload=1000, bed_length=6, bed_width=4, bed_height=2),
    Car("Tesla", "S", "MUSK 1", location="LA", mileage=75000),
    Truck("Toyota", "Hilux", "Z23 45X", payload=2000, bed_length=8,bed_width=4,bed_height=2)
    ]

rentals = [
    Rental(vehicles[0], driverID="DI001", duration=1),
    Rental(vehicles[1], driverID="DI002", duration=5),
    Rental(vehicles[2], driverID="DI003", duration=2),
    Rental(vehicles[3], driverID="DI004", duration=1),
]

for rental in rentals:
    print(rental.generate_invoice())
    print("----")

