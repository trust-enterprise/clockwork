class Product_Bill:
    def __init__(self, price, discount_percent = 0):
        self.price = price
        self.discount_percent = discount_percent #this is a setter
    
    @property
    def discount_percent(self):
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self, discount_percent_new):
        if 0 <= discount_percent_new <= 50:
            self._discount_percent = discount_percent_new
        else:
            raise ValueError("discount percent range is 0 to 50% max")

    @property
    def final_bill(self):
        return self.price*(1-self._discount_percent/100)
    
prodA = Product_Bill(300, 10)
print(prodA.final_bill)

prodA.discount_percent = 20
print(prodA.final_bill)


# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
    
#     @property
#     def email(self):
#         return f"{self.first}.{self.last}@gmail.com"
    
#     @email.setter
#     def email(self, value):
#         first, last  = value.split("@")[0].split('.')
#         self.first = first
#         self.last  = last

#     @email.deleter
#     def email(self):
#         self.first = None
#         self.last = None


# emp = Employee("Aman", "Verma")    
# print(emp.email)

# emp.email = "aman.gupta@gmail.com"
# print(emp.first)
# print(emp.last)

# del emp.email
# print(emp.first)
# print(emp.last)
