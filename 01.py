class User:
    platform_name = "skillgrow"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def profile(self):
        return f"{self.name , self.email}"
    
    @classmethod 
    def change_platform(cls, new_platform_name):
        cls.platform_name = new_platform_name

    @staticmethod
    def is_email_valid(email):
        return "@" in email
    

class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.enrolled_courses = []

    def enroll(self, course_name):
        self.enrolled_courses.append(course_name)

class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.course_uploaded = []

    def upload_course(self, course_name):
        self.course_uploaded.append(course_name)

s1 = Student("Aman", "aman@gmail.com")
i1 = Instructor("Ravi", "ravi@gmail.com")

s1.enroll("Python Basics")
i1.upload_course("Python Basics")

print(s1.profile())
print(i1.profile())

print(User.platform_name)
User.change_platform("SkillGrow Pro")
print(s1.enrolled_courses)
print(i1.platform_name)





