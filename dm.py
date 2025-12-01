class Staff:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Car:
    def __init__(self, title, model, price, year):
        self.title = title
        self.model = model
        self.price = price
        self.year = year

class Taxipark:
    def __init__(self, title):
        self.title = title
        self.cars = []
        self.staffs = []

    def add_car(self):
        title = input("title: ")
        model = input("model: ")
        price = input("price: ")
        year = input("year: ")
        car = Car(title, model, price, year)
        car.__init__(title, model, price, year)
        self.cars.append(car)

    def add_staff(self):
        name = input("name: ")
        age = input("age: ")
        staff = Staff(name, age)
        staff.__init__(name, age)
        self.staffs.append(staff)

    def delete_staff(self):
        name = input("name: ")
        for item in self.staffs:
            if item.name == name:
                self.staffs.remove(item)
                print("staff deleted")

    def delete_car(self):
        title = input("title: ")
        model = input("model: ")
        for item in self.cars:
            if item.title == title and item.model == model:
                self.cars.remove(item)
                print("car deleted")

    def view_staff(self):
        count = 0
        for item in self.staffs:
            count += 1
            print(f"{count}. name:{item.name}, age:{item.age}")

    def view_car(self):
        count = 0
        for item in self.cars:
            count += 1
            print(f"{count}. title:{item.title}, model:{item.model}, price:{item.price}, year:{item.year}")

class Busy(Taxipark):
    def __init__(self, title):
        super().__init__(title)
        self.busy_car = []
        self.busy_staff = []

    def add_busy_car(self):
        title = input("title: ")
        model = input("model: ")
        for item in self.cars:
            if item.title == title and item.model == model:
                self.cars.remove(item)
                self.busy_car.append(item)
                print("car busy")

    def delete_busy_car(self):
        title = input("title: ")
        model = input("model: ")
        for item in self.busy_car:
            if item.title == title and item.model == model:
                self.busy_car.remove(item)
                self.cars.append(item)
                print("success")

    def view_busy_cars(self):
        count = 0
        for item in self.busy_car:
            count += 1
            print(f"{count}. title:{item.title}, model:{item.model}, price:{item.price}, year:{item.year}")

    def view_busy_staff(self):
        count = 0
        for item in self.busy_staff:
            count += 1
            print(f"{count}. name:{item.name}, age:{item.age}")


class AdminManager:
    def __init__(self):
        self.taxipark = Busy("MyTaxi")
        self.taxipark.__init__("MyTaxi")

        self.users = {
            "admin": {"password": "0000", "role": "admin", "name": "Admin Boss", "age": 30},
            "user": {"password": "0001", "role": "user", "name": "Ali", "age": 20}
        }

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        if username in self.users and self.users[username]["password"] == password:
            print("Login successful")
            return self.users[username]["role"]

        print("Error: Wrong username or password")
        return None

    def view_user_info(self, username):
        user = self.users[username]
        print("\n--- Sizning ma'lumotlaringiz ---")
        print(f"Username: {username}")
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")
        print(f"Password: {user['password']}")

    def edit_user_info(self, username):
        print("\n--- Ma'lumotlarni o'zgartirish ---")
        user = self.users[username]

        new_name = input(f"Yangi ism ({user['name']}): ") or user['name']
        new_age = input(f"Yangi yosh ({user['age']}): ") or user['age']
        new_password = input(f"Yangi password ({user['password']}): ") or user['password']

        user["name"] = new_name
        user["age"] = new_age
        user["password"] = new_password

        print("Ma'lumotlar yangilandi!")

    def run_user_menu(self, username):
        while True:
            print("\nUser Menu")
            print("1. Bo'sh mashinalarni ko'rish")
            print("2. Ma'lumotlarimni ko'rish")
            print("3. Ma'lumotlarimni o'zgartirish")
            print("0. Chiqish")

            choice = input("Tanlang: ")

            if choice == "1":
                self.taxipark.view_car()

            elif choice == "2":
                self.view_user_info(username)

            elif choice == "3":
                self.edit_user_info(username)

            elif choice == "0":
                break

            else:
                print("Noto'g'ri tanlov!")

    def run_admin_menu(self):
            while True:
                print("\nAdmin Menu")
                print("1. Car qo'shish")
                print("2. Staff qo'shish")
                print("3. Car o'chirish")
                print("4. Staff o'chirish")
                print("5. Bo'sh carlar")
                print("6. Busy car qo'shish")
                print("7. Busy carni qaytarish")
                print("8. Busy carlarni ko'rish")
                print("0. Chiqish")

                choice = input("Tanlang: ")

                if choice == "1":
                    self.taxipark.add_car()
                elif choice == "2":
                    self.taxipark.add_staff()
                elif choice == "3":
                    self.taxipark.delete_car()
                elif choice == "4":
                    self.taxipark.delete_staff()
                elif choice == "5":
                    self.taxipark.view_car()
                elif choice == "6":
                    self.taxipark.add_busy_car()
                elif choice == "7":
                    self.taxipark.delete_busy_car()
                elif choice == "8":
                    self.taxipark.view_busy_cars()
                elif choice == "0":
                    break
                else:
                    print("Noto‘g‘ri tanlov")

    def run(self):
        username = input("Username: ")
        password = input("Password: ")

        if username in self.users and self.users[username]["password"] == password:
            role = self.users[username]["role"]
            print("Login successful")

            if role == "admin":
                self.run_admin_menu()
            else:
                self.run_user_menu(username)  # <--- argument qo'shildi

        else:
            print("Login xato!")

manager = AdminManager()
manager.run()