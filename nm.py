import uuid

class Product:
    def __init__(self, title, price=0.0, count=0):
        self.id = str(uuid.uuid4())
        self.title = title
        self.price = float(price)
        self.count = float(count)
        self.type = ''

class Card:
    def __init__(self, serial, password, balance=0.0):
        self.balance = balance
        self.serial = serial
        self.password = password

class PurchaseHistory:
    def __init__(self, user, product, count, total_price, date):
        self.id = str(uuid.uuid4())
        self.user = user
        self.product = product
        self.count = count
        self.total_price = total_price
        self.date = date
        self.purchased = False

class User:
    def __init__(self, username, password, phone, is_admin=False, is_user=True):
        self.username = username
        self.password = password
        self.phone = phone
        self.is_admin = is_admin
        self.is_user = is_user
        self.cards = []
        self.cart = []
        self.purchase_history = []

class Market:
    def __init__(self, title):
        self.title = title
        self.balance = 0.0
        self.users = []
        self.products = []
        self.purchase_history = []

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"{product.title} qo‘shildi")

    def view_all_products(self):
        if not self.products:
            print("Hozircha mahsulotlar mavjud emas")
        for item in self.products:
            print(f"{item.title} | {item.price} | {item.count} | {item.type}")

    def view_products_by_type(self, p_type):
        found = False
        for item in self.products:
            if item.type == p_type:
                print(f"{item.title} | {item.price} | {item.count}")
                found = True
        if not found:
            print(f"Bu turdagi mahsulotlar mavjud emas: {p_type}")

    def delete_product(self, title):
        for item in self.products:
            if item.title == title:
                self.products.remove(item)
                print(f"{title} o‘chirildi")
                return
        print("Mahsulot topilmadi")

    def update_product(self, title, field, new_value):
        for item in self.products:
            if item.title == title:
                if field == "title":
                    item.title = new_value
                elif field == "price":
                    item.price = float(new_value)
                elif field == "count":
                    item.count = float(new_value)
                elif field == "type":
                    item.type = new_value
                else:
                    print("Noto‘g‘ri maydon")
                    return
                print(f"{field} yangilandi")
                return
        print("Mahsulot topilmadi")

class Water(Product):
    def init(self, title, price, count):
        super().init(title, price, count)
        self.type = 'suv'

class Food(Product):
    def init(self, title, price, count):
        super().init(title, price, count)
        self.type = 'ovqat'

class MobilePhone(Product):
    def init(self, title, price, count):
        super().init(title, price, count)
        self.type = 'mobil telefon'

market = Market("MeningBozorim")

def market_manager(market: Market):
    while True:
        kod = input(
            "1. Suv qo‘shish\n"
            "2. Ovqat qo‘shish\n"
            "3. Mobil telefon qo‘shish\n"
            "4. Mahsulotlarni ko‘rish\n"
            "5. Mahsulot o‘chirish\n"
            "6. Mahsulotni yangilash\n"
            "7. Chiqish\n"
            "Tanlov: "
        )
        if kod == '1':
            title = input("Mahsulot nomi: ")
            price = float(input("Narxi: "))
            count = float(input("Soni: "))
            market.add_product(Water(title, price, count))
        elif kod == '2':
            title = input("Mahsulot nomi: ")
            price = float(input("Narxi: "))
            count = float(input("Soni: "))
            market.add_product(Food(title, price, count))
        elif kod == '3':
            title = input("Mahsulot nomi: ")
            price = float(input("Narxi: "))
            count = float(input("Soni: "))
            market.add_product(MobilePhone(title, price, count))
        elif kod == '4':
            view_choice = input("1. Barcha mahsulotlar\n2. Tur bo‘yicha ko‘rish\nTanlov: ")
            if view_choice == '1':
                market.view_all_products()
            elif view_choice == '2':
                type_choice = input("1. suv\n2. ovqat\n3. mobil telefon\nTanlov: ")
                type_map = {'1': 'suv', '2': 'ovqat', '3': 'mobil telefon'}
                if type_choice in type_map:
                    market.view_products_by_type(type_map[type_choice])
        elif kod == '5':
            title = input("O‘chiriladigan mahsulot nomi: ")
            market.delete_product(title)
        elif kod == '6':
            title = input("Yangilanishi kerak mahsulot nomi: ")
            field_choice = input("1. nom\n2. narx\n3. soni\n4. tur\nTanlov: ")
            field_map = {'1':'title','2':'price','3':'count','4':'type'}
            if field_choice in field_map:
                new_value = input("Yangi qiymatni kiriting: ")
                market.update_product(title, field_map[field_choice], new_value)
        elif kod == '7':
            break

market_manager(market)