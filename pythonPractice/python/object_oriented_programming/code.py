""""
student = {"name":"Rolf","grades":(89,45,35,24,99)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))
"""

class Student:
    def __init__(self):
        self.name="Rolf"
        self.grade=(90,91,65,23)

    def average(self):
        return sum(self.grade) / len(self.grade)

student = Student()
print(student.name)
print(student.grade)
print(student.average())

#__str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"
bob=Person("Bob",35)
print(bob) # prints "hello" instead of "Person(name='Bob', age=35

#3
