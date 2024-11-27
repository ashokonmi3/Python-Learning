class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    @property
    def email(self): #emp1.email
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    def apply_bonus(self):
        bonus = self.salary * 0.10  # Applying a 10% bonus
        self.salary += bonus
