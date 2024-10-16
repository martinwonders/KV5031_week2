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

class Car(Vehicle):
    def __init__(self, make, model, license_plate, driver_id="000", mileage=0, location="", seats=4, notes=""):
        super().__init__(make, model, license_plate, driver_id, mileage, location, seats, notes)

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"

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

vehicles = [
    Car("Toyota", "Corolla", "ABC123", location="New York", mileage=10000),
    Truck("Ford", "F-150", "XYZ789", payload=1000, bed_length=6, bed_width=4, bed_height=2),
    Car("Tesla", "S", "MUSK 1", location="LA", mileage=75000),
    Truck("Toyota", "Hilux", "Z23 45X", payload=2000, bed_length=8,bed_width=4,bed_height=2)
    ]

for vehicle in vehicles:
    print(vehicle.display_info())

