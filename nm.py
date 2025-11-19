import re
class Product:
    def __init__(self, title, price, year):
        self.title = title
        self.price = price
        self.year = year
        self.type=''

class Shop:
    def __init__(self, title, phone):
        self.title = title
        self.phone = phone
        self.baza=[]

    def add_water(self):
        title=input('title:')
        price=int(input('price:'))
        year=int(input('year:'))
        p1=Product(title,price,year)
        p1.type='water'
        self.baza.append(p1)

    def add_food(self):
        title=input('title:')
        price=int(input('price:'))
        year=int(input('year:'))
        p1=Product(title,price,year)
        p1.type='food'
        self.baza.append(p1)

    def add_mobilephone(self):
        title=input('title:')
        price=int(input('price:'))
        year=int(input('year:'))
        p1=Product(title,price,year)
        p1.type='mobile phone'
        self.baza.append(p1)

    def view_all(self):
        for item in self.baza:
            print(f'title:{item.title} price:{item.price} year:{item.year}')

    def delete_products(self):
        title2=input('title:')
        a=self.baza
        for item in a:
            if item.title==title2:
                a.remove(item)

    def update_product(self):
        title2 = input("Tahrirlamoqchi bo'lgan product title: ")

        for item in self.baza:
            if item.title == title2:
                print("Qaysi maydonni yangilaysiz?")
                print("1. Title")
                print("2. Price")
                print("3. Year")
                print("4. Type (water / food / mobile phone)")
                choice = input("Tanlov: ")

                if choice == "1":
                    new_title = input("Yangi title: ")
                    item.title = new_title
                    print("Title yangilandi!")

                elif choice == "2":
                    new_price = int(input("Yangi price: "))
                    item.price = new_price
                    print("Narx yangilandi!")

                elif choice == "3":
                    new_year = int(input("Yangi year: "))
                    item.year = new_year
                    print("Year yangilandi!")

                elif choice == "4":
                    new_type = input("Yangi type (water/food/mobile phone): ")
                    item.type = new_type
                    print("Type yangilandi!")

                else:
                    print("Noto'g'ri tanlov!")
                return

        print("Bu nomdagi product topilmadi!")

    def view_product(self):
        type3=input('type:')
        for item in self.baza:
            if item.type==type3:
                print(f'title:{item.title} price:{item.price} year:{item.year}')

shop1=Shop('shop1',12354789)

def shop_manager(shop:Shop):
    while True:
        kod=input("1. add water \n2. add food \n3. add mobile phone \n4. view product \n5. delete product \n6. update product")
        if kod=='1':
            shop.add_water()
        elif kod=='2':
            shop.add_food()
        elif kod=='3':
            shop.add_mobilephone()
        elif kod=='4':
            while True:
                kod1=input("1. view all \n2. view through type \n3. exit\n")
                if kod1=='1':
                    shop.view_all()
                elif kod1=='2':
                    shop.view_product()
                else:
                    break
        elif kod=='5':
            shop.delete_products()
        elif kod=='6':
            shop.update_product()

shop_manager(shop1)