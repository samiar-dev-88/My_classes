class Person:

    def __init__(self,name,age):
        self.esm = name
        self.sen = age

    def sleep(self):
        print(self.esm , "is sleeping...")

class Student(Person):

    classs = "201"

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        print(self.esm_s , "is studing...")


p1 = Person("ali",9)
p2 = Person("sami",14)
s1 = Student("alii" , 8)

print(s1.esm)