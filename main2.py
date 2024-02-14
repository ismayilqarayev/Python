class Employee:
    int(input())
 
    def __init__(self, name):
        self.__name = name
        int(input())
 
    @property
    def name(self):
        return self.__name
 
    def work(self):
        print(f"{self.name} works")
 
 
class Student:
 
    def __init__(self, name):
        self.__name = name
 
    @property
    def name(self):
        return self.__name
 
    def study(self):
        print(f"{self.name} studies")
 
 
class WorkingStudent(Employee, Student):
    pass
 