import json


def all_card():
    with open("bankomat.json","r") as f:
        try:
            data = json.load(f)
            return dict(data)
        except:
            print("fayl bo'sh")
            return False

def add_all(d:dict):
    data = all_card()
    if data!=False:
        data.update(d)
        with open("bankomat.json","w") as f:
            json.dump(data,f,indent=4)
    else:
        with open("bankomat.json","w") as f:
            json.dump(d,f,indent=4)
def add_card():
    while True:
        cardnum = input("Raqamni kiriting: ").strip().replace(" ", "")
        if cardnum.isdigit() and len(cardnum) == 16:
            break
        print("Karta raqami 16 ta raqam bo‘lishi kerak. Qayta kiriting.")

    while True:
        code = input("Kodni kiriting: ").strip()
        if code.isdigit() and len(code) == 4:
            break
        print("Kod 4 ta raqam bo‘lishi kerak. Qayta kiriting.")

    name = input("Ismni kiriting: ").strip()
    balance = input("Balansni kiriting: ").strip()

    card = {
        cardnum: {
            "card number": cardnum,
            "code": code,
            "phone number": None,
            "balance": balance,
            "Card owner": name
        }
    }

    data = all_card()
    if cardnum in data:
        print("Bu karta allaqachon mavjud.")
        return

    data.update(card)
    add_(data)
    print("Karta muvaffaqiyatli qoʻshildi.")
def add_(data:dict):
    with open("bankomat.json","w") as f:
        json.dump(data,f,indent=4)


def delete_card():
    cardnum = input("Karta raqamini kiriting: ")
    code = input("Kodni kiriting: ")

    data = all_card()
    if not data:
        print("Fayl bo'sh yoki card topilmadi")
        return

    if cardnum in data:
        if data[cardnum]["code"] == code:
            del data[cardnum]
            add_(data)
            print("Card o'chirildi")
        else:
            print("Kod noto'g'ri")
    else:
        print("Card topilmadi")

def view_card_info():
    cardnum = input("Karta raqamini kiriting: ")
    code = input("Kodini kiriting: ")

    data = all_card()
    if not data:
        print("Fayl bo'sh yoki card topilmadi")
        return

    if cardnum in data:
        if data[cardnum]["code"] == code:
            print("Card ma'lumotlari:")
            for key, value in data[cardnum].items():
                print(f"{key}: {value}")
        else:
            print("Kod noto'g'ri")
    else:
        print("Card topilmadi")

def update_balance():
    cardnum = input("Enter card number: ")
    code = input("Enter code: ")

    data = all_card()
    if cardnum in data:
        if data[cardnum]["code"] == code:
            print(f"Hozirgi balansingiz: {data[cardnum]['balance']}")
            choice = input("qoshish yoki yechish?: ").lower()
            try:
                amount = float(input("summani kiriting: "))
            except ValueError:
                print("Invalid amount")
                return

            if choice == "qoshish":
                data[cardnum]["balance"] = str(float(data[cardnum]["balance"]) + amount)
                print(f"Balansingiz: {data[cardnum]['balance']}")
            elif choice == "yechish":
                if float(data[cardnum]["balance"]) >= amount:
                    data[cardnum]["balance"] = str(float(data[cardnum]["balance"]) - amount)
                    print(f"Balansingiz: {data[cardnum]['balance']}")
                else:
                    print("Mablag' yetarli emas")
            else:
                print("Noto'g'ri")

            add_(data)
        else:
            print("Kod noto'g'ri")
    else:
        print("Karta topilmadi")

def link_sms_service():
    cardnum = input("Karta raqamini kiriting: ")
    code = input("Kodini kiriting: ")

    data = all_card()
    if cardnum in data:
        if data[cardnum]["code"] == code:
            if data[cardnum]["phone number"] is not None:
                print(f"Telefon raqamingiz allaqachon ulangan: {data[cardnum]['phone number']}")
                return
            phone = input("SMS xizmatiga ulash uchun telefon raqamingizni kiriting: ")
            data[cardnum]["phone number"] = phone
            add_(data)  # yangilangan ma’lumotni json faylga yozish
            print("SMS xizmati muvaffaqiyatli ulandi!")
        else:
            print("Kod noto‘g‘ri")
    else:
        print("Karta topilmadi")

    def card_manager():
        while True:
            print(" 1.Karta qo'shish yoki yangilash \n 2.Kartani o'chirish \n 3.Karta bo'yicha xizmatlar \n ")
            kod = input("")
            if kod == "1":
                add_card()
            elif kod == "2":
                delete_card()
            if kod == "3":
                while True:
                    print(
                        " 1.Pul yechish/qo'shish \n 2.Karta ma'lumotlarini ko'rish \n 3.SMS xizmatiga ulash \n 4.Chiqish \n ")
                    kod1 = input("")
                    if kod1 == "1":
                        update_balance()
                    elif kod1 == "2":
                        view_card_info()
                    elif kod1 == "3":
                        link_sms_service()
                    else:
                        break

    card_manager()