class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary 

employee1 = Employee("Tjabo", 44, "Kingen", 44000)
employee2 = Employee("AG", 66, "Queen Coleen", 66000)

print(employee1.name)
print(employee2.name)

