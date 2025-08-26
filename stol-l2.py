class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.K = 9550 #кВт
    
    def info(self):
        print('бренд', self.brand,)
        print('модель', self.model,)
        print('год', self.year,)

class Car(Vehicle):
        def __init__(self, fuel_type, max_speed, engine_capacity, rotation_speed, torque_moment):
            self.fuel_type = fuel_type
            self.max_speed = max_speed
            self.engine_capacity = engine_capacity
            self.rotation_speed = rotation_speed
            self.torque_moment = torque_moment
    
        def info(self):
            print('тип топлива', self.fuel_type,)
            print('максимальная скорость', self.max_speed,)
            print('емкость двигателя', self.engine_capacity,)
            print('скорость вращения (об/мин)', self.rotation_speed,)
            print('крутящий момент', self.torque_moment,)
            
            
        def engine_power_calc(self):
            self.P = (self.rotation_speed  * self.torque_moment) / 9550
            print('мощность двигателя(кВт): ',self.P,)
            
        def __del__(self):
            print('удалено')
        
            
def left():
    brand = str(input(" введите бренд: " ))
    model = str(input(" введите модель: " ))
    year = int(input(" введите год: " ))
    fuel_type = str(input(" введите тип топлива: " ))
    max_speed = int(input(" введите максимальную скорость: " ))
    engine_capacity = int(input(" введите емкость двигателя : " ))
    rotation_speed = int(input(" введите скорость вращения (об/мин): " ))
    torque_moment = int(input(" введите крутящий момент (Ньютон-метр): " ))
    carr = Vehicle(brand, model, year,)
    carr = Car(fuel_type, max_speed, engine_capacity, rotation_speed, torque_moment)
    carr.info()
    carr.engine_power_calc()

def main():
    left()   
    
if __name__ == '__main__':

    main()       
    