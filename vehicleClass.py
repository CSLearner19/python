#create class
class Vehicle:
    #create init method
    def __init__(self, max_speed, mileage):
        #bind arguments
        self.max_speed = max_speed
        self.mileage = mileage
#object creation
modelX = Vehicle(240,18)
#access variables inside the init method
print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:",modelX.mileage)