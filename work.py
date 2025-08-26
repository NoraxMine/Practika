#Deros.all rights reserved.
#==========================


class Employee():
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        print(f'Имя работника:{self.name},\nпозиция:{self.position},\nз\п:{self.salary}')
    
    def calc_salary(self):
        w_d  = int(input('Введите число отработанных дней: '))
        print(f'Зарплата за этот месяц:{w_d * int(self.position) * int(self.salary)}')

    def __del__(self):
        print('Работник удален')


class Manager(Employee):
    def __init__(self, name, position, salary, department,num_employees):
        super().__init__(name, position, salary)
        self.department = department
        self.num_employees = num_employees

    def info(self):
        super().info()
        print(f'кол-во сотрудников: {self.num_employees},\nдепортамет:{self.department}')
    
    def calc_salary(self):
        w_d  = int(input('Введите число отработанных дней: '))
        print(f'Зарплата за этот месяц:{w_d * int(self.position) * int(self.salary) + w_d * int(self.position) * int(self.salary) * (1/int(self.num_employees))}')

    def __del__(self):
        print('Менеджер удален')

def main():
    rb = Employee('Fox', '12', '23')
    rb.info()
    rb.calc_salary()
    mn  = Manager('kail', '23', '34', 'dep', '9')
    mn.info()
    mn.calc_salary()


if __name__ == '__main__':
    main()