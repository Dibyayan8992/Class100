class Car(object):
    def __init__(self, model, colour, company, speedlimit):
        self.model = model
        self.colour = colour
        self.company = company
        self.speedlimit = speedlimit
    def start(self):
        print("Started")
    def stop(self):
        print("Stopped")
    def accelerate(self):
        print("Accelerating")
    def changeGear(self, geartype):
        print("Gear Changed")
venue = Car("SX", "Red", "Hyundai", 120)
print(venue.speedlimit)
print(venue.colour)
xuv = Car(500, "Black", "Mahindra", "200")
print(xuv.speedlimit)
print(xuv.colour)