import csv

contacts_file = "contacts.csv"
sms_file = "sent_sms.csv"

def init_sms_file():
    try:
        with open(sms_file, "x", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["To", "Message"])
    except FileExistsError:
        pass

def send_sms():
    try:
        with open(contacts_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            contacts = [row[0].strip() for row in reader if len(row) >= 2 and row[0].strip() != ""]
            if not contacts:
                print("Kontaktlar mavjud emas. SMS yuborib bo‘lmaydi.")
                return
    except FileNotFoundError:
        print("Kontaktlar fayli topilmadi.")
        return

    recipient = input("Kimga yuborilsin (ismni kiriting): ").strip()
    if recipient not in contacts:
        print("Bunday kontakt mavjud emas")
        return

    message = input("Xabar matnini kiriting: ").strip()

    init_sms_file()
    with open(sms_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([recipient, message])

    print("Xabar muvaffaqiyatli yuborildi")

def view_sent_sms():
    try:
        with open(sms_file, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                print("Hozircha yuborilgan SMS yo‘q.")
                return
            print("Yuborilgan SMSlar:")
            for row in reader[1:]:
                print(f"Kimga: {row[0]}, Xabar: {row[1]}")
    except FileNotFoundError:
        print("Hozircha yuborilgan SMS yo‘q.")

def sms_manager():
    init_sms_file()
    while True:
        print("========= SMS Manager =========")
        print("1. SMS yuborish")
        print("2. Yuborilgan SMSlarni ko‘rish")
        print("3. Chiqish")

        choice = input("Tanlovingiz: ")

        if choice == "1":
            send_sms()
        elif choice == "2":
            view_sent_sms()
        elif choice == "3":
            print("SMS Managerdan chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov, qayta urinib ko‘ring.")

sms_manager()