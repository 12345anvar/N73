import re
class Contacts:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

Contact=Contacts('Ali','998885556644', 'google@gmail.com')
base=[Contact]
def add_contact(s:list):
    a=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
    b=r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
    while True:
        name = input("Name: ")
        if name.isalpha():
            phonenumber = input("Phone number: ")
            if re.fullmatch(a,phonenumber):
                email = input("Email: ")
                if re.fullmatch(b,email):
                    contact = Contacts(name, phonenumber, email)
                    s.append(contact)
                    break
                else:
                     print("Emailingiz xato, iltimos qayta kiriting!")
            else:
                print("Telefon raqamingiz xato, iltimos qayta kiriting!")
        else:
            print("Noto'g'ri, iltimos qayta kiriting!")
# add_contact(base)

def delete_contact(s:list):
        name = input("O'chirmoqchi bo'lgan kontakt ismi: ")
        for i, contact in enumerate(s):
            if contact.name.lower() == name.lower():
                s.pop(i)
                print(f"{name} o'chirildi!")
                return
        print("Bunday ism topilmadi!")
# delete_contact(base)

def update_contact(s: list):
    a = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
    b = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

    name_search = input("Tahrirlash uchun kontakt ismi: ")
    for contact in s:
        if contact.name.lower() == name_search.lower():
            print("Qaysi birini yangilamoqchisiz?")
            print("1. Name")
            print("2. Phone number")
            print("3. Email")
            choice = input("Tanlang: ")

            if choice == "1":
                new_name = input("Yangi ism: ")
                if new_name.isalpha():
                    contact.name = new_name
                    print("Ism yangilandi!")
                else:
                    print("Xato: faqat harf kiriting")
            elif choice == "2":
                new_phone = input("Yangi telefon raqam: ")
                if re.fullmatch(a, new_phone):
                    contact.phone_number = new_phone
                    print("Telefon raqam yangilandi!")
                else:
                    print("Xato: noto'g'ri telefon raqam")
            elif choice == "3":
                new_email = input("Yangi email: ")
                if re.fullmatch(b, new_email):
                    contact.email = new_email
                    print("Email yangilandi!")
                else:
                    print("Xato: noto'g'ri email")
            else:
                print("Noto'g'ri tanlov")
            return
    print("Bunday kontakt topilmadi!")
# update_contact(base)

def view_contacts(s:list):
    count=0
    for item in s:
        count+=1
        print(f'{count}. name:{item.name}, Phone numbere:{item.phone_number}, email:{item.email}')
# view_contact(base)

def contact_manager():
    while True:
        print(" 1. Kontakt qo'shish \n 2. Kontakni o'chirish \n 3. Kontaktlarni ko'rish \n 4. Kontaktni tahrirlash")
        kod = int(input('Tanlang: '))
        if kod == 1:
            add_contact(base)
        elif kod == 3:
            view_contacts(base)
        elif kod == 2:
            delete_contact(base)
        elif kod == 4:
            update_contact(base)

contact_manager()
