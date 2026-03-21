
class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is ", self.name)

class Student(Person):

    def __init__(self, name, teacher_name):
        super().__init__(name)
        self.teacher_name = teacher_name

    def greet(self):
        print("Hello, my name is ", self.name, "and I am a student.")

    def custom_greeting(self, message):
        print("My teacher", self.teacher_name,  "says", message)

class Teacher(Person):
    def greet(self):
        print("Hello, my name is ", self.name, "and I am a teacher.")

p1 = Person("John")
s1 = Student("Michael", "Luisa")
t1 = Teacher("Luisa")

print("____ PERSON ____")
p1.greet()

print("\n____ STUDENT ____")
s1.greet()
s1.custom_greeting("Today I will learn Python")

print("\n____ Teacher ____")
t1.greet()
