class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id
    def set_name(self, name):
        self.__name = name
    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        print(f"Employee ID: {self.__emp_id}")
        print(f"Name: {self.__name}")
        print(f"Salary: ₹{self.__salary}")

    def give_hike(self, percentage):
        if percentage > 0:
            hike_amount = self.__salary * (percentage / 100)
            self.__salary += hike_amount
            print(f"Salary hiked by {percentage}%. New salary is ₹{self.__salary:.2f}")
        else:
            print("Percentage should be positive")


# Demonstration
emp1 = Employee("E001", "Ravi Kumar", 40000)
emp1.display_info()
emp1.give_hike(10)
emp1.display_info()