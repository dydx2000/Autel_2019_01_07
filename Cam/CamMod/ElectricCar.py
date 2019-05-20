class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=35

    def get_descriptive_name(self):
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self,mileage):
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
             print("You can't roll back an odometer!")
             
    def increment_odometer(self,miles):
        self.odometer_reading += miles
              
class ElectricCar(Car):
    def __str__(self):
        return "I'm a car"

    # def __int__(self,make,model,year):
    def __init__(self,make,model,year):


        super(ElectricCar,self).__init__(make,model,year)


        self.a=35



    def describe_battery(self):

        print(self.a)

t = ElectricCar('PORSCHE','911GT','2018')
my_tesla=ElectricCar('tesla\t','x\t','2019\t')


print(t.get_descriptive_name())
print(my_tesla.get_descriptive_name())
t.describe_battery()
my_tesla.describe_battery()
print(str(t))

