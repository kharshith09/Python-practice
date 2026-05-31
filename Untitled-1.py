# densities = {"steel": 7850, "aluminum": 2700, "copper": 8960,"titanium":4500}
# while True:
#     inp= input("select the metal(or type 'q to quit) ")

#     if inp == "q":
#         break

#     if inp  in densities:
#         print("the desnisty of the material is: ",densities[inp])
#     else:
#         print("Material not found")

# class rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width*self.height   
#     def perimeter(self):
#         return 2*(self.width+self.height)
    
# r1 = rectangle(5,3)
# print(r1.area())
# print(r1.perimeter())

# r2 = rectangle(10, 4)
# print(r2.area())
# print(r2.perimeter())

# class Laptop:
#     def __init__(self, ram, rom):
#         self.ram = ram
#         self.rom = rom

#     def display(self):
#         print("the laptop has", self.ram, "GB of RAM and", self.rom, "GB of ROM")

#     def upgrade_ram(self, new_ram):
#         self.ram = new_ram


# l1 = Laptop(8, 256)
# l1.display()
# l1.upgrade_ram(16)
# l1.display()


# class GamingLaptop(Laptop):
#     def __init__(self, ram, rom, gpu):
#         super().__init__(ram, rom)
#         self.gpu = gpu

#     def display(self):
#         super().display()
#         print("the laptop has", self.gpu, "GPU")

#     def show_gpu(self):
#         print(f"the laptop has {self.gpu} GPU")


# g = GamingLaptop(16, 512, "NVIDIA RTX 3080")
# g.display()
# g.show_gpu()



# class sensor:
#     def __init__(self,name):
#         self.name = name
#     def read_value(self):    
#         print(f"Reading value from {self.name} sensor")

# class temperaturesensor(sensor):
#     def __init__(self,name,unit):
#         super().__init__(name)
#         self.unit = unit

#     def read_value(self):
#         super().read_value()
#         print(f"Temperature value is in {self.unit}")

# sensor1 = sensor("Generic")
# sensor1.read_value()
# temp_sensor = temperaturesensor("Temperature", "Celsius")
# temp_sensor.read_value()
