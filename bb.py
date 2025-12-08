class Shop:
    def __init__(self):
        self.products = []
        self.users = []

shop = Shop()  # global shop

class Product:
    def __init__(self, title, brend_name, price, type, count):
        self.title = title
        self.brend_name = brend_name
        self.price = price
        self.type = type
        self.count = count

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_product(self):
        title = input("title: ")
        brend_name = input("brend name: ")
        price = input("price: ")
        type = input("type: ")
        count = int(input("count: "))
        p = Product(title, brend_name, price, type, count)
        shop.products.append(p)
        print("Product added")

    def remove_product(self):
        title = input("title: ")
        brend_name = input("brend: ")
        type = input("type: ")
        for item in shop.products:
            if item.title == title and item.brend_name == brend_name and item.type == type:
                shop.products.remove(item)
                print("Product removed")
                return
        print("Product not found")

    def edit_product(self):
        title = input("title: ")
        brend_name = input("brend: ")
        for item in shop.products:
            if item.title == title and item.brend_name == brend_name:
                item.title = input("new title: ")
                item.brend_name = input("new brend name: ")
                item.price = input("new price: ")
                item.type = input("new type: ")
                item.count = int(input("new count: "))
                print("Product edited")
                return
        print("Product not found")

    def view_usersinfo(self):
        for idx, u in enumerate(shop.users, 1):
            print(f"{idx}. username:{u.username}, email:{u.email}, phone:{u.phone}, balance:{u.balance}")

    def login_admin(self):
        while True:
            print("""
1. Add Product
2. Remove Product
3. Edit Product
4. View Users
5. Exit
            """)
            kod = input(">>> ")
            if kod == "1":
                self.add_product()
            elif kod == "2":
                self.remove_product()
            elif kod == "3":
                self.edit_product()
            elif kod == "4":
                self.view_usersinfo()
            elif kod == "5":
                break
            else:
                print("Invalid choice")

class User:
    def __init__(self, username, password, email, balance, phone):
        self.username = username
        self.password = password
        self.email = email
        self.balance = balance
        self.phone = phone
        self.box = []

    def menu_user(self):
        while True:
            print("""
1. Buy Product
2. View Products
3. Cart
4. Profile
5. Exit
            """)
            choice = input(">>> ")
            if choice == "1":
                self.busket_product()
            elif choice == "2":
                self.view_products()
            elif choice == "3":
                self.frombusket_buy()
            elif choice == "4":
                print(f"username:{self.username}, email:{self.email}, phone:{self.phone}, balance:{self.balance}")
            elif choice == "5":
                break
            else:
                print("Invalid choice")

    def user_register(self):
        username = input("username: ")
        password = input("password: ")
        email = input("email: ")
        phone = input("phone: ")
        u = User(username, password, email, 0, phone)
        shop.users.append(u)
        print("Registration successful")
        u.menu_user()

    def user_login(self):
        username = input("username: ")
        password = input("password: ")

        if username == "admin" and password == "123":
            admin = Admin("admin", "123")
            admin.login_admin()
            return

        for u in shop.users:
            if u.username == username and u.password == password:
                u.menu_user()
                return
        print("Invalid login")


    def view_products(self):
        if not shop.products:
            print("No products")
        for idx, p in enumerate(shop.products, 1):
            print(f"{idx}. {p.title}, {p.brend_name}, {p.price}, {p.type}, count:{p.count}")

    def busket_product(self):
        if not shop.products:
            print("No products")
            return
        self.view_products()
        choice = input("Select product index >>> ")
        try:
            idx = int(choice)-1
            prod = shop.products[idx]
            if prod.count > 0:
                self.box.append(Product(prod.title, prod.brend_name, prod.price, prod.type, 1))
                prod.count -= 1
                print(f"{prod.title} added to cart")
                if prod.count == 0:
                    shop.products.remove(prod)
            else:
                print("Product out of stock")
        except:
            print("Invalid choice")

    def frombusket_buy(self):
        if not self.box:
            print("Cart is empty")
            return

        while True:
            total = sum(int(p.price) for p in self.box)
            print(f"Cart items:")
            for idx, p in enumerate(self.box, 1):
                print(f"{idx}. {p.title}, {p.price}")
            print(f"Total price: {total}")

            print("""
    1. Buy all products
    2. Remove product
    3. Back to menu
            """)
            choice = input(">>> ")

            if choice == "1":
                if self.balance >= total:
                    self.balance -= total
                    self.box.clear()
                    print("Purchase successful")
                else:
                    print("Insufficient balance")
            elif choice == "2":
                rem = input("Enter product index to remove >>> ")
                try:
                    idx = int(rem) - 1
                    if 0 <= idx < len(self.box):
                        self.box.pop(idx)
                        print("Product removed from cart")
                    else:
                        print("Invalid index")
                except:
                    print("Invalid input")
            elif choice == "3":
                break
            else:
                print("Invalid choice")

def start_menu():
    while True:
        print("""
1. Register
2. Login
        """)
        choice = input(">>> ")
        if choice == "1":
            u = User("", "", "", 0, "")
            u.user_register()
        elif choice == "2":
            u = User("", "", "", 0, "")
            u.user_login()
        else:
            print("Invalid choice")

start_menu()

