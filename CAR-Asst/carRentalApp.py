from car import Car, PetrolCar, DieselCar, ElectricCar, HybridCar
from customer import Customer
from carrental import CarRental

class CarRentalApp(object):
    
    ## create car objects
    global car, petrolCar, dieselCar, electricCar, hybridCar, carRental
    car = Car()
#    engineCar = EngineCar()
    petrolCar = PetrolCar()
    dieselCar = DieselCar()
    electricCar = ElectricCar()
    hybridCar = HybridCar()
    carRental = CarRental()
    
    ## create customer object
    global customer
    customer = Customer()
    
    
    def fleetInfo():
        ## construct car fleet
        carRental.setFleet(40)
        fleet = carRental.getFleet()
        availablePetrol = int(0.50 * fleet)
        availableDiesel = int(0.20 * fleet)
        availableElectric = int(0.10 * fleet)
        availableHybrid = int(0.20 * fleet)
        
        carRental.setAvailablePetrolCars([])
        carRental.setAvailableDieselCars([])
        carRental.setAvailableElectricCars([])
        carRental.setAvailableHybridCars([])
        for p in range(1, availablePetrol+1):
            carRental.availablePetrolCars.append(petrolCar)
        for d in range(1, availableDiesel+1):
            carRental.availableDieselCars.append(dieselCar)
        for e in range(1, availableElectric+1):
            carRental.availableElectricCars.append(electricCar)
        for h in range(1, availableHybrid+1):
            carRental.availableHybridCars.append(hybridCar)
            
    
    def customerDetails():
    
        ## print quit message
        print 'Type "q" to quit this program'
   
        ## obtain input form user   
        while True:
            name = raw_input('Enter Customer name please: ')
            if name == 'q' or name == 'Q':
                quit()
            if name.isalpha() == False:
                print 'Sorry, Please try again.'
                continue
            customer.setName(name)
            print 'Type "H" for hire a car from the fleet.'
            print 'Type "R" for a car to the fleet.'
            global hireReturn
            hireReturn = raw_input('Hire or Return?: ') 
            if hireReturn == 'q':
                quit()
            hireReturn = hireReturn.lower()
            if (hireReturn != 'h') and (hireReturn != 'r'): 
                print 'Invalid input.  Please try again.'
                continue
            break
        return hireReturn
    
    
    def carInfo():
        ## obtain car choice
        while True:
            print 'What type of car is being hired or returned?:'
            print 'Type "P" for petrol'
            print 'Type "D" for diesel'
            print 'Type "E" for electric'
            print 'Type "H" for hybrid'
            global carChoice
            carChoice = raw_input('Enter car type now: ')
            carChoice = carChoice.lower()
            if carChoice == 'q':
                quit()
            carChoiceOptions = ['p', 'd', 'e', 'h']
            ## check for valid carChoice
            if carChoice not in carChoiceOptions:
                print 'Invalid car choice.  Please try agsin.'
                continue
            ## check if car choice available
            if hireReturn == 'h': 
                if ( (carChoice == 'p') and (len(carRental.getAvailablePetrolCars()) <= 0) ) \
                or ( (carChoice == 'd') and (len(carRental.getAvailableDieselCars()) <= 0) ) \
                or ( (carChoice == 'e') and (len(carRental.getAvailableElectricCars()) <= 0) ) \
                or ( (carChoice == 'h') and (len(carRental.getAvailableHybridCars()) <= 0) ):
                    print 'Sorry, there are none of this car type currently in the fleet.'
                    print 'Please choose alternative car type.'
                    continue
            break
        return carChoice
    
    def carMakeInfo():
        ##obtain car make info
        while True:
            if hireReturn == 'h':
                print 'Does Customer prefer a Ford or a Toyota?:'
                print 'Type "F" for Ford'
                print 'Type "T" for Toyota'
                makeChoice = raw_input('Enter Make preference: ')
                makeChoice = makeChoice.lower()    
                if makeChoice == 'q':
                    quit()
                makeChoiceOptions = ['f', 't']
                ## check for valid makeChoice
                if makeChoice not in makeChoiceOptions:
                    print 'Invalid Make choice.  Please try again.'
                    continue
                if makeChoice == 'f':
                    car.setMake('Ford')
                if makeChoice == 't':
                    car.setMake('Toyota')
            break
    
    def carModelInfo():
        ##obtain car model info
        while True:
            if car.getMake() == 'Ford':
                print 'Does Customer prefer a Focus or a Mondeo?:'
                print 'Type "F" for Focus'
                print 'Type "M" for Mondeo'
                modelChoice = raw_input('Enter Model preference: ')
                modelChoice = modelChoice.lower()    
                if modelChoice == 'q':
                    quit()
                modelChoiceOptions = ['f', 'm']
                ## check for valid modelChoice
                if modelChoice not in modelChoiceOptions:
                    print 'Invalid Model choice.  Please try agsin.'
                    continue
                if modelChoice == 'f':
                    car.setModel('Focus')
                if modelChoice == 'm':
                    car.setModel('Mondeo')
            break
        while True:
            if car.getMake() == 'Toyota':
                print 'Does Customer prefer a Corolla or an Avensis?:'
                print 'Type "C" for Corolla'
                print 'Type "A" for Avensis'
                modelChoice = raw_input('Enter Model preference: ')
                modelChoice = modelChoice.lower()    
                if modelChoice == 'q':
                    quit()
                modelChoiceOptions = ['c', 'a']
                ## check for valid modelChoice
                if modelChoice not in modelChoiceOptions:
                    print 'Invalid make choice.  Please try agsin.'
                    continue
                if modelChoice == 'c':
                    car.setModel('Corolla')
                if modelChoice == 'a':
                    car.setModel('Avensis')
            break
    
    def petrolCarInfo():
        ##obtain fuel info
        while True:
            if carChoice == 'p':
                print 'Does Customer have a fuel preference?:'
                print 'Type "L" for leaded'
                print 'Type "U" for unleaded'
                fuelChoice = raw_input('Enter Customer choice now: ')
                fuelChoice = fuelChoice.lower()    
                if fuelChoice == 'q':
                    quit()
                fuelChoiceOptions = ['l', 'u']
                ## check for valid fuelChoice
                if fuelChoice not in fuelChoiceOptions:
                    print 'Invalid fuel choice.  Please try agsin.'
                    continue
                if fuelChoice == 'l':
                    petrolCar.setPetrolType('Leaded')
                if fuelChoice == 'u':
                    petrolCar.setPetrolType('Unleaded')
            break
        
    def dieselCarInfo():
        ##obtain turbo info
        while True:
            if carChoice == 'd':
                print 'Does Customer prefer standard or turbo?:'
                print 'Type "S" for standard'
                print 'Type "T" for turbo'
                turboChoice = raw_input('Enter Customer choice now: ')
                turboChoice = turboChoice.lower()    
                if turboChoice == 'q':
                    quit()
                turboChoiceOptions = ['s', 't']
                ## check for valid turboChoice
                if turboChoice not in turboChoiceOptions:
                    print 'Invalid turbo choice.  Please try agsin.'
                    continue
                if turboChoice == 's':
                    dieselCar.setDieselTurbo(False)
                if turboChoice == 't':
                    dieselCar.setDieselTurbo(True)
            break
        
    def electricCarInfo():
        ##obtain fuelCells info
        while True:
            if carChoice == 'e':
                print 'Does Customer prefer battery or capacitor?:'
                print 'Type "B" for battery'
                print 'Type "C" for capacitor'
                fuelCellsChoice = raw_input('Enter Customer choice now: ')
                fuelCellsChoice = fuelCellsChoice.lower()    
                if fuelCellsChoice == 'q':
                    quit()
                fuelCellsChoiceOptions = ['b', 'c']
                ## check for valid fuelCellsChoice
                if fuelCellsChoice not in fuelCellsChoiceOptions:
                    print 'Invalid fuel cell choice.  Please try agsin.'
                    continue
                if fuelCellsChoice == 'b':
                    electricCar.setFuelCells('Battery')
                if fuelCellsChoice == 'c':
                    electricCar.setFuelCells('Capacitor')
            break
    
    def hybridCarInfo():
        ##obtain brake info
        while True:
            if carChoice == 'h':
                print 'Does Customer prefer standard or regenerative braking system?:'
                print 'Type "S" for standard brake system'
                print 'Type "R" for regenerative brake system'
                brakeChoice = raw_input('Enter Customer choice now: ')
                brakeChoice = brakeChoice.lower()    
                if brakeChoice == 'q':
                    quit()
                brakeChoiceOptions = ['s', 'r']
                ## check for valid brakeChoice
                if brakeChoice not in brakeChoiceOptions:
                    print 'Invalid brake choice.  Please try agsin.'
                    continue
                if brakeChoice == 's':
                    hybridCar.setHybridBrake(False)
                if brakeChoice == 'r':
                    hybridCar.setHybridBrake(True)
            break
    
    def updateFleet(carChoice, hireReturn):
        ## remove/add one (1) car to/from fleet
        fleet = carRental.getFleet()
        if carChoice == 'p':
            if (hireReturn == 'h'):
                carRental.availablePetrolCars.pop()
                fleet -= 1
            elif (hireReturn == 'r'):
                carRental.availablePetrolCars.append(petrolCar)
                fleet += 1
            else:
                print 'Hell has just frozen over.  Petrol debug necessary!'
                quit()
        elif carChoice == 'd':
            if (hireReturn == 'h'):
                carRental.availableDieselCars.pop()
                fleet -= 1
            elif (hireReturn == 'r'):
                carRental.availableDieselCars.append(dieselCar)
                fleet += 1
            else:
                print 'Hell has just frozen over.  Diesel debug necessary!'
                quit()
        elif carChoice == 'e':
            if (hireReturn == 'h'):
                carRental.availableElectricCars.pop()
                fleet -= 1
            elif (hireReturn == 'r'):
                carRental.availableElectricCars.append(electricCar)
                fleet += 1
            else:
                print 'Hell has just frozen over.  Electric debug necessary!'
                quit()
        elif carChoice == 'h':
            if (hireReturn == 'h'):
                carRental.availableHybridCars.pop()
                fleet -= 1
            elif (hireReturn == 'r'):
                carRental.availableHybridCars.append(hybridCar)
                fleet += 1
            else:
                print 'Hell has just frozen over.  Hybrid debug necessary!'
                quit()
        else:
            print 'Woah ... back up the apple-cart.  Debug required now!'
            quit()

            
    def calculateHirePeriod(hireReturn):
        while True:
            print 'How many days does Customer require?'
            print 'Number must be between 1 and 28 (inclusive).'
            hirePeriod = raw_input('Please enter number of days: ')
            if hirePeriod == 'q':
                quit()
            try:
                hirePeriod = int(hirePeriod)
                if (1 <= hirePeriod) and (hirePeriod <= 28):
                    break
                else:
                    print 'Hire period must be between 1 and 28.'
            except:
                print "Invalid input.  Try again."
        return hirePeriod
        
     
    def calculateHireCharge(hireReturn, hirePeriod):
        
        if hirePeriod <= 10:
            if (car.getModel() == 'Avensis') or (car.getModel() == 'Mondeo'):
                hireCharge = hirePeriod * 60.00
            if (car.getModel() == 'Corolla') or (car.getModel() == 'Focus'):
                hireCharge = hirePeriod * 50.00
        elif (10 < hirePeriod) and (hirePeriod <= 28):
            if (car.getModel() == 'Avensis') or (car.getModel() == 'Mondeo'):
                hireCharge = 500 + ((hirePeriod - 10) * 30.00)
            if (car.getModel() == 'Corolla') or (car.getModel() == 'Focus'):
                hireCharge = 400 + ((hirePeriod - 10) * 20.00)
        else:
            print "we shouldn't be here!"
            quit()
        return hireCharge
    
    fleetInfo()
    hireReturn = customerDetails()
    carInfo()
    carMakeInfo()
    carModelInfo()
    petrolCarInfo()
    dieselCarInfo()
    electricCarInfo()
    hybridCarInfo()
    availableCars = updateFleet(carChoice, hireReturn)
    
    if hireReturn == 'h':
        customer.hirePeriod = calculateHirePeriod(hireReturn)
        customer.hireCharge = calculateHireCharge(hireReturn, customer.hirePeriod)
    
    print 'Customer name:\t\t\t', customer.getName()
    if hireReturn == 'r':
        print 'Thanks for returning the car.'
    if hireReturn == 'h':
        print 'Make of car hired:\t\t', car.getMake()
        print 'Model of car hired:\t\t', car.getModel()
#        print 'Transmission of car hired:\t', Car.getTransmission()
        if carChoice == 'p':
            print 'Petrol type:\t\t\t', petrolCar.getPetrolType()
        if carChoice == 'd':
            print 'Has turbo?:\t\t\t', dieselCar.getDieselTurbo()
        if carChoice == 'e':
            print 'Fuel cell type:\t\t\t', electricCar.getFuelCells()
        if carChoice == 'h':
            print 'Regenerative braking system:\t', hybridCar.getHybridBrake()
        print 'Hire period (days):\t\t', customer.hirePeriod
        print 'Hire charge (euro):\t\t', customer.hireCharge