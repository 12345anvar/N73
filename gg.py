# class Person:
#     def __init__(self, name, age, phone):
#         self.name = name
#         self.age = age
#         self.phone = phone
#
#     def show(self):
#         print(f'name{self.name}, age{self.age}, phone{self.phone}')
#
#
# class Student(Person):
#     def __init__(self, name, age, phone, student_id, group):
#         super().__init__(name, age, phone)
#         self.student_id = student_id
#         self.group = group
#     def show(self):
#         print(f'name{self.name}, age{self.age}, phone{self.phone}, student_id{self.student_id}, group{self.group}')
#
#
# p1=Person('ali', "23", "2564563123")
# s1=Student('vali', "53", "256134563123", 565454, 312123)
# p1.show()
# s1.show()
from itertools import count
from os import remove


class Student:
    def __init__(self, name, pohone, age, email):
        self.name = name
        self.pohone = pohone
        self.age = age
        self.email = email


class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []

    def add_student(self, student):
        name = str(input("name:"))
        pohone = int(input("pohone:"))
        age = int(input("age:"))
        email = input("email:")
        student= Student(name, pohone, age, email)
        self.students.append(student)

    def view_students(self):
        count = 0
        for item in self.students:
            count += 1
            print(f"{count}. name:{item.name} pohone:{item.pohone} age:{item.age} email:{item.email}")

    def edit_student(self):
        name = str(input("name:"))
        for item in self.students:
            if item.name == name:
                item.name = input("name:")
                item.pohone = int(input("pohone:"))
                item.age = int(input("age:"))
                item.email = input("email:")
            else:
                 print("Student not found")

    def deleat_student(self):
        name = str(input("name:"))
        for item in self.students:
            if item.name == name:
                self.students.remove(item)
            else:
                print("Student not found")

class OTM:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def add_group(self):
        title = input("grupa nomini kiriting:")
        profession = input("professionni kiriting:")
        group = Group(title, profession)
        self.groups.append(group)

    def view_groups(self):
        count = 0
        for item in self.groups:
            count += 1
            print(f"{count}. title:{item.title}, profession:{item.profession}")

    def edit_group(self):
        title = input("Titleni kiriting:")
        for item in self.groups:
            if item.title == title:
                item.title = input("title:")
                item.profession = input("professionni kiriting:")
                break
            else:
                print("Group not found")

    def deleat_group(self):
        title = input("Titleni kiriting:")
        for item in self.groups:
            if item.title == title:
                self.groups.remove(item)
            else:
                print("Group not found")

class ERP:
    def __init__(self):
        self.title = "ERP"
        self.OTMs = []



    def add_OTM(self):
        title = input("OTM ni kiriting:")
        otm = OTM(title)
        self.OTMs.append(otm)

    def view_OTMs(self):
        count =0
        for otm in self.OTMs:
            count+=1
            print(f'{count}. {otm.title}')

    def edit_OTM(self):
        title = input("Titleni kiriting:")
        for item in self.OTMs:
            if item.title == title:
                item.title = input("title:")
            else:
                print("OTM not found")

    def deleat_OTM(self):
        title = input("Titleni kiriting:")
        for item in self.OTMs:
            if item.title == title:
                self.OTMs.remove(item)
            else:
                print("OTM not found")

erp=ERP()
def OTM_manager(group:ERP):
    while True:
        print("=========")
        kod=input("1.add otm \n2.view otm \n3.edit otm \n4.deleat otm \n5.exit\n")
        if kod=="1":
            group.add_OTM()
        elif kod=="2":
            group.view_OTMs()
        elif kod=="3":
            group.edit_OTM()
        elif kod=="4":
            group.deleat_OTM()
        else:
            break
def group_manager(group:OTM):
    while True:
        print("=========")
        kod=input("1.add group \n2.view group \n3.edit group \n4.delete group \n5.exit\n")
        if kod=="1":
            group.add_group()
        elif kod=="2":
            group.view_groups()
        elif kod=="3":
            group.edit_group()
        elif kod=="4":
            group.deleat_group()
        else:
            break
def student_manager(student:Group):
    while True:
        print("=========")
        kod=input("1.add student\n2.view student\n3.edit student\n4.delete student\n5.exit\n")
        if kod=="1":
            student.add_student()
        elif kod=="2":
            student.view_students()
        elif kod=="3":
            student.edit_student()
        elif kod=="4":
            student.deleat_student()
        else:
            break
def erp_manager(ep):
    while True:
        print("=============")
        kod = input(" 1. OTM \n 2.Group \n 3.Student \n")
        if kod =='1':
            erp_manager(ep)
        elif kod =='2':
            group_manager(ep)
        elif kod =='3':
            student_manager(ep)

erp_manager(erp)

