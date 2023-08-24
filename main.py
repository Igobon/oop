
# Створити ієрархію класів для опису академії.
#
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
#
# Продумати архітектуру: реалізувати принципи ООП








class Academy:
    def __init__(self,name_of_academy):

        self.name_of_academy=name_of_academy

    def show_info(self):
        print(f'Name of academy: {self.name_of_academy} ')

class Mark:
    def __init__(self,mark):
        self.mark=mark

    def show_info(self):
        print(f'Mark: {self.mark}')




class Subject:
    def __init__(self,subject):
        self.subject=subject

    def show_info(self):
        print(f'Subject name: {self.subject}')



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_info(self):
        print(f' Name {self.name}\nAge {self.age}')

class Teacher(Person,Subject):
    def __init__(self,name,age,subject,salary):
        Person.__init__(self,name,age)
        Subject.__init__(self,subject)
        self.salary=salary


    def show_info(self):

        print(f'Teacher {self.name} age {self.age} profesor of {self.subject} have salary {self.salary}')

class Student(Academy,Person,Mark):
    def __init__(self,name,age,name_of_academy,mark):
        Person.__init__(self, name, age)
        Academy.__init__(self, name_of_academy)
        Mark.__init__(self,mark)


    def show_info(self):
        print(f'{self.name} age{self.age} from {self.name_of_academy} university have mark{self.mark}')





sb=Subject("Math")
sb.show_info()
ac=Academy("Technikal",)
ac.show_info()
pr=Person("Igor",26)
pr.show_info()
tc=Teacher("Anton Petrovich", 42,"Math",12567)
tc.show_info()
st=Student("Igor",28,"Technikal",100)


st.show_info()




