# Creating class Car and defining public variables
class Car(object):

    def __init__(self):
        self.make = ''
        self.model = ''
        self.transmission = ''
        self.petrolType = ''
        self.turbo = ''
        self.fuelCells = ''
        self.regenerativeBrake = ''

    ## setting function
    def setMake(self, make):
        self.make = make
        
    def setModel(self, model):
        self.model = model

    ## getting function
    def getMake(self):
        return self.make
        
    def getModel(self):
        return self.model
		
	


# Creating class for each Car and defining private variables       
class PetrolCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.petrolType = ''
    
    def setPetrolType(self, petrolType):
        self.petrolType = petrolType

    def getPetrolType(self):
        return self.petrolType

# Creating class for each Car and defining private variables        
class DieselCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.turbo = False
        
    def setDieselTurbo(self, turbo):
        self.turbo = turbo

    def getDieselTurbo(self):
        return self.turbo

# Creating class for each Car and defining private variables        
class ElectricCar(Car):
    def __init__(self):
        Car.__init__(self)
        self.fuelCells = ''
        
    def setFuelCells(self, fuelCells):
        self.fuelCells = fuelCells

    def getFuelCells(self):
        return self.fuelCells

# Creating class for each Car and defining private variables
class HybridCar(PetrolCar, ElectricCar):
    def __init__(self):
        PetrolCar.__init__(self)
        ElectricCar.__init__(self)
        self.regenerativeBrake = False
    
    def setHybridBrake(self, regenerativeBrake):
        self.regenerativeBrake = regenerativeBrake

    def getHybridBrake(self):
        return self.regenerativeBrake