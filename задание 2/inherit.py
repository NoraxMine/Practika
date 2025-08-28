class Component:


    def __init__ (self, motherboard_model, power_unit_model, power_unit_port, motherboard_soccet, motherboard_voltage_port):
        self.motherboard_model = motherboard_model
        self.power_unit_model = power_unit_model
        self.power_unit_port = power_unit_port
        self.motherboard_soccet = motherboard_soccet
        self.motherboard_voltage_port = motherboard_voltage_port

    def get_info(self):  
        if  self.power_unit_port == self.motherboard_voltage_port:
            print("Совместимы")
        else: 
            print("Не совместимы")
    
    def check_compatibility(self): 
        print(f'motherboard_model:{self.motherboard_model}, power_unit_model:{self.power_unit_model}, power_unit_port:{self.power_unit_port}, motherboard_soccet:{self.motherboard_soccet}, motherboard_voltage_port:{self.motherboard_voltage_port}')

    


class Processor(Component):
    def __init__(self, motherboard_model, power_unit_model, power_unit_port, motherboard_soccet, motherboard_voltage_port, core_count, power_consumption, processor_model, soccet):
        super().__init__(motherboard_model, power_unit_model, power_unit_port, motherboard_soccet, motherboard_voltage_port)
        self.core_count = core_count
        self.power_consumption = power_consumption
        self.processor_model = processor_model
        self.soccet = soccet

    def get_info2(self):        
        print(f"core_count:{self.core_count}, power_consumption:{self.power_consumption}, processor_model:{self.processor_model}, soccet:{self.soccet}")

    def check_system_compatibility(self):   
        if self.soccet == self.motherboard_soccet:
            print("Совместимо")
        else:
            print("Не совместимо")  

def __del__ (self):
        print("dell done")

def func():
    info = Component(13,23,65,54,65)
    info.get_info()
    info.check_compatibility()
    info2 = Processor(13,23,65,54,65, 5, 6, 85, 54)
    info2.get_info2()
    info2.check_system_compatibility()

def main():
    func()

if __name__ == '__main__':
    main()
