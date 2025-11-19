class Contact:
    def init(self, ism, phone):
        self.ism = ism
        self.phone = phone

class SMSManager:
    def init(self):
        self.kontaktlar = []
        self.sent_sms = []

    def add_contact(self, ism, phone):
        for c in self.kontaktlar:
            if c.ism.lower() == ism.lower():
                print("Bunday kontakt allaqachon mavjud")
                return
        self.kontaktlar.append(Contact(ism, phone))
        print(f"{ism} kontakt sifatida qo‘shildi")

    def view_contacts(self):
        if not self.kontaktlar:
            print("Kontaktlar mavjud emas")
            return
        print("Kontaktlar ro‘yxati:")
        for c in self.kontaktlar:
            print(f"{c.ism} - {c.phone}")

    def send_sms(self):
        if not self.kontaktlar:
            print("Kontaktlar mavjud emas. SMS yuborib bo‘lmaydi.")
            return
        recipient_name = input("Kimga yuborilsin (ismni kiriting): ").strip()
        recipient = None
        for c in self.kontaktlar:
            if c.ism.lower() == recipient_name.lower():
                recipient = c
                break
        if not recipient:
            print("Bunday kontakt mavjud emas")
            return
        message = input("Xabar matnini kiriting: ").strip()
        self.sent_sms.append((recipient.ism, message))
        print("Xabar muvaffaqiyatli yuborildi")

    def view_sent_sms(self):
        if not self.sent_sms:
            print("Hozircha yuborilgan SMS yo‘q")
            return
        print("Yuborilgan SMSlar:")
        for to, msg in self.sent_sms:
            print(f"Kimga: {to}, Xabar: {msg}")

def sms_manager():
    sms = SMSManager()
    while True:
        print("========= SMS Manager =========")
        print("1. Kontakt qo‘shish")
        print("2. Kontaktlarni ko‘rish")
        print("3. SMS yuborish")
        print("4. Yuborilgan SMSlarni ko‘rish")
        print("5. Chiqish")
        choice = input("Tanlovingiz: ").strip()
        if choice == "1":
            ism = input("Kontakt ismi: ").strip()
            phone = input("Telefon raqami: ").strip()
            sms.add_contact(ism, phone)
        elif choice == "2":
            sms.view_contacts()
        elif choice == "3":
            sms.send_sms()
        elif choice == "4":
            sms.view_sent_sms()
        elif choice == "5":
            print("SMS Managerdan chiqildi")
            break
        else:
            print("Noto‘g‘ri tanlov, qayta urinib ko‘ring")

sms_manager()