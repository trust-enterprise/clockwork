class User():
    def __init__(self, name, email) :
        self.name = name
        self.email = email
        self.is_active = True

    def password_reset(self):
        print (f"Password has been reset for {self.name}")
    
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)

    def ban(self):
        self.is_active = False
        self.enrolled_courses.clear()
        print (f"{self.name} is banned")

class Admin(User):
    def password_strength(self, password):
        print ("Strong password" if len(password) >= 8 else "Weak password")

    def ban_user(self, user):
        user.ban()

stu1 = Student("aman", "aman@gmail.com")
stu1.enroll_course("IT402")
print(stu1.enrolled_courses)


admin1 = Admin("a","a@b.com")
admin1.password_strength("asdfjlkjg")
admin1.password_reset()
admin1.ban_user(stu1)
print(admin1.mro())
