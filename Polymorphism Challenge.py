# Super simple classes
class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing ⛵"

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Show how each moves
for vehicle in vehicles:
    print(vehicle.move())
