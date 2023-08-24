
# Створити ієрархію класів для опису академії.
#
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
#
# Продумати архітектуру: реалізувати принципи ООП








class Academy:
    def __init__(self,name_of_academy):

        self._name_of_academy=name_of_academy

    def show_info(self):
        print(f'Name of academy: {self._name_of_academy} ')
    @property
    def name_of_academy(self):
        return self._name_of_academy
    @name_of_academy.setter
    def name_of_academy(self,new_name):
        self._name_of_academy=new_name


class Mark:
    def __init__(self,mark):
        self._mark=mark
    def show_info(self):
        print(f'Mark: {self._mark}')
    def getter_mark(self):
        return self._mark







class Subject:
    def __init__(self,subject):
        self._subject=subject

    def show_info(self):
        print(f'Subject name: {self._subject}')
    def getter_subject(self):
        return self._subject

    def setter_subject(self,new_subject):
        self._subject=new_subject




class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    def show_info(self):
        print(f' Name {self._name}\nAge {self._age}')
    def getter_name(self):
        return self._name
    def setter_name(self,new_name):
        self._name= new_name
    def getter_age(self):
        return self._age
    def setter_age(self,new_age):
        self._age= new_age
class Teacher(Person,Subject):
    def __init__(self,name,age,subject,salary):
        Person.__init__(self,name,age)
        Subject.__init__(self,subject)
        self.__salary=salary
    def getter_salary(self):
        return self.__salary


    def show_info(self):

        print(f'Teacher {self._name} age {self._age} profesor of {self._subject} have salary {self.__salary}')

class Student(Academy,Person,Mark):
    def __init__(self,name,age,name_of_academy,mark):
        Person.__init__(self, name, age)
        Academy.__init__(self, name_of_academy)
        Mark.__init__(self,mark)


    def show_info(self):
        print(f'{self._name} age{self._age} from {self._name_of_academy} university have mark{self._mark}')





subject=Subject("Math")
subject.show_info()
subject.setter_subject("Physics")
subject.show_info()
academy=Academy("Technikal",)
academy.show_info()
person=Person("Igor",26)
person.show_info()
teacher=Teacher("Anton Petrowich",42,"Math",12567)
teacher.show_info()
student=Student("Igor",28,"Technikal",100)
student.show_info()




