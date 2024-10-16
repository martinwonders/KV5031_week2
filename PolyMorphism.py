# Base class
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Subclass for Full-Time Employees
class FullTimeEmployee(Employee):
    def __init__(self, name, fixed_salary):
        super().__init__(name)
        self.fixed_salary = fixed_salary

    def calculate_salary(self):
        return self.fixed_salary


# Subclass for Part-Time Employees
class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked



employees = [
    FullTimeEmployee("Jane Doe", 45000),
    PartTimeEmployee("Alice Cooper", 350, 100),
    FullTimeEmployee("John Smith", 36000),
    PartTimeEmployee("Diana Morgan", 275, 80)
]

# Polymorphism in action: calculating salaries for different types of employees
# Calculate and print salaries
for employee in employees:
    print(f"{employee.name}: £{employee.calculate_salary()}")
