# class Person:
#     def __init__(self, name, age, surname):
#         self.name = name
#         self.age = age
#         self.surname = surname
#
#     def show(self):
#         print(f'name;{self.name}\nage:{self.age}\nsurname:{self.surname}')
#
# class Student(Person):
#     def __init__(self, name, age, surname, student_id, group):
#         super().__init__(name, age, surname)
#         self.student_id = student_id
#         self.group = group
#
# s1=Student('ali', 24, 'vali', 456789, 25)
# s1.show()
# from itertools import count


# class da vorislik 5 xil turi bor

class Card:
    def __init__(self, owner, seria, balans, password, phone):
        self.owner = owner
        self.seria = seria
        self.balans = balans
        self.password = password
        self.phone = ''
card1=Card('ali',1321654654, 100000, 0000,'')
class ATM:
    def __init__(self,bank):
        self.bank = bank
        self.cards = []

    def add_card(self):
        seria=int(input("karta raqamini kiriting:"))
        owner=str(input("karta egasi ismi:"))
        balans=0
        phone=''
        password=int(input("karta parolini kiriting:"))
        a=Card(owner,seria,balans,password,phone)
        self.cards.append(a)

    def delete_card(self):
        seria=int(input("karta raqamini kiriting:"))
        password=int(input("karta parolini kiriting:"))
        a=self.cards
        count=0
        while True:
            for item in a:
                if item.seria == seria:
                    if item.password == password:
                        if count<4:
                            a.remove(item)
                            print("Karta o'chirildi")
                            break
                        else:
                            break
                            print("Karta bloklandi")
                    else:
                        print("parol noto'g'ri")
                        count+=1
                else:
                    print("Bunday karta mavjud emas")

    def update_password(self):
        seria=int(input("karta raqamini kiriting:"))
        password=int(input("karta parolini kiriting:"))
        a=self.cards
        count=0
        while True:
            for item in a:
                if item.seria == seria:
                    if item.password == password:
                        if count<4:
                            newpassword=int(input("Yangi parolni kiriting:"))
                            item.password=newpassword
                            print("Parol almashtirildi")
                            break
                        else:
                            break
                            print("Karta bloklandi")
                    else:
                        print("parol noto'g'ri")
                        count+=1
                else:
                    print("Bunday karta mavjud emas")

    def add_balans(self):
        seria=int(input("karta raqamini kiriting:"))
        password=int(input("karta parolini kiriting:"))
        a=self.cards
        count=0
        while True:
            for item in a:
                if item.seria == seria:
                    if item.password == password:
                        if count<4:
                            add=int(input("balansni kiriting:"))
                            b=item.balans+add
                            item.balans=b
                        else:
                            break
                            print("Karta bloklandi")
                    else:
                        print("Parol noto'g'ri")
                        count+=1
                else:
                    print("Bunday karta mavjud emas")
    def m_balans(self):
        seria=int(input("karta raqamini kiriting:"))
        password=int(input("karta parolini kiriting:"))
        a=self.cards
        count=0
        while True:
            for item in a:
                if item.seria == seria:
                    if item.password == password:
                        if count<4:
                            m=int(input("balansni kiriting:"))
                            b=item.balans-m
                            item.balans=b
                        else:
                            break
                            print("Karta bloklandi")
                    else:
                        print("Parol noto'g'ri")
                        count+=1
                else:
                    print("Bunday karta mavjud emas")

    def connect_sms(self):
        seria=int(input("karta raqamini kiriting:"))
        password=int(input("karta parolini kiriting:"))
        a=self.cards
        count=0
        while True:
            for item in a:
                if item.seria == seria:
                    if item.password == password:
                        if count<4:
                            newphone=input("1. sms xizmatini ulash 2. sms xizmatini o'chirish")
                            if newphone == '1':
                                item.phone='ha'
                                print("Sms xizmati ulandi")
                            elif newphone == '2':
                                item.phone='yoq'
                        else:
                            break
                            print("Karta bloklandi")
                    else:
                        print("Parol noto'g'ri")
                        count+=1
                else:
                    print("Bunday karta mavjud emas")
    def view_cards(self):
        count=1
        for item in self.cards:
            print(f'{count}. owner={item.owner} seria={item.seria} balans={item.balans} phone={item.phone} password={item.password}')
            count+=1

atm=ATM('NBU')

def bankomat_manager(atm:ATM):
    while True:
        kod=input("1.add card \n2.delete card \n3.add balans \n4.view cards \n5.sms \n6.update password \n7.withdraw balance")
        if kod == '1':
            atm.add_balans()
        elif kod == '2':
            atm.delete_card()
        elif kod == '3':
            atm.add_balans()
        elif kod == '4':
            atm.view_cards()
        elif kod == '5':
            atm.connect_sms()
        elif kod == '6':
            atm.update_password()
        elif kod == '7':
            atm.m_balans()
        else:
            print("notogri qayta kiriting")

bankomat_manager(atm)