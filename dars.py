import csv
import re

telefon_regex = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
filename = "contacts.csv"

def init_file():
    try:
        with open(filename, "x", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone"])
    except FileExistsError:
        pass

def add_contact():
    name = input("Ismni kiriting: ")
    while True:
        phone = input("Telefon raqamini kiriting: ")
        if re.fullmatch(telefon_regex, phone):
            break
        else:
            print("Telefon raqami noto‘g‘ri formatda. Qaytadan kiriting.")

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone])
    print("Kontakt muvaffaqiyatli qo‘shildi.")

def view_contacts():
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                print("Hozircha kontaktlar mavjud emas.")
                return
            print("Kontaktlar ro‘yxati:")
            for row in reader[1:]:
                print(f"Ism: {row[0]}, Telefon: {row[1]}")
    except FileNotFoundError:
        print("Hozircha kontaktlar mavjud emas.")

def delete_contact():
    name = input("O‘chirmoqchi bo‘lgan kontakt ismini kiriting: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                print("Hozircha kontaktlar mavjud emas.")
                return
            header = reader[0]
            rows = reader[1:]
    except FileNotFoundError:
        print("Hozircha kontaktlar mavjud emas.")
        return

    new_rows = [header]
    found = False
    for row in rows:
        if row[0].lower() == name.lower():
            found = True
        else:
            new_rows.append(row)

    if not found:
        print("Bunday ism topilmadi.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)
    print("Kontakt o‘chirildi.")

def edit_contact():
    name = input("Tahrirlash uchun kontakt ismini kiriting: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                print("Hozircha kontaktlar mavjud emas.")
                return
            header = reader[0]
            rows = reader[1:]
    except FileNotFoundError:
        print("Hozircha kontaktlar mavjud emas.")
        return

    found = False
    for i in range(len(rows)):
        if rows[i][0].lower() == name.lower():
            found = True
            print(f"Hozirgi ma'lumot: Ism: {rows[i][0]}, Telefon: {rows[i][1]}")
            new_name = input("Yangi ism kiriting (bo‘sh qoldirsangiz o‘zgarmaydi): ")
            while True:
                new_phone = input("Yangi telefon kiriting (bo‘sh qoldirsangiz o‘zgarmaydi): ")
                if new_phone == "" or re.fullmatch(telefon_regex, new_phone):
                    break
                else:
                    print("Telefon raqami noto‘g‘ri formatda.")
            if new_name != "":
                rows[i][0] = new_name
            if new_phone != "":
                rows[i][1] = new_phone
            break

    if not found:
        print("Bunday ism topilmadi.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print("Kontakt muvaffaqiyatli yangilandi.")

def contact_manager():
    init_file()
    while True:
        print("========= Kontakt Manager =========")
        print("1. Yangi kontakt qo‘shish")
        print("2. Kontaktlarni ko‘rish")
        print("3. Kontaktni o‘chirish")
        print("4. Kontaktni tahrirlash")
        print("5. Chiqish")
        choice = input("Tanlovingiz: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            print("Dasturdan chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov, qayta urinib ko‘ring.")

contact_manager()