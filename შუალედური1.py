class Person:
    def __init__(self,name,gender,age,salary):
        self.name = name
        self.gender = gender
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"my name is{self.name},i'm{self.gender},my age is{self.age} and my salary is{self.salary}"
    def total_monthly_salary(self):
        income_tax = self.salary*0.2
        pension_tax = self.salary*0.001
        total_month_salary = income_tax + pension_tax
        return total_month_salary
    def pension_savings(self):
        saving = self.total_monthly_salary()-self.salary*0.2
        if self.gender == "male" and self.age<=29 and self.age >= 65:
            return saving
        if self.gender == "famale" and self.age<=29 and self.age >= 60:
            return saving
        # return self.pension_savings()
    # def pensiaze_gasvla(self):
    #     if self.gender == "male":
    #         return დრო არ მეყოოოო ავირიეე

pers1 = Person("Tekla","gogo",20,100)
print(pers1.total_monthly_salary())
print(pers1.pension_savings())


