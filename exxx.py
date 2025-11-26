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
    def __init__(self,title):
        self.title = title
        self.cars=[]
        self.staffs = []

    def add_car(self):
        title = input("title:")
        model = input("model:")
        price = input("price:")
        year = input("year:")
        self.cars.append(Car(title, model, price, year))

    def add_staff(self):
        name = input("name:")
        age = input("age:")
        self.staffs.append(Staff(name, age))

    def delete_staff(self):
        name = input("name:")
        for item in self.staffs:
            if item.name == name:
                self.staffs.remove(item)
                print("staff deleted")

    def delete_car(self):
        title = input("title:")
        model = input("model:")
        for item in self.cars:
            if item.title == title:
                if item.model == model:
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
        title = input("title:")
        model = input("model:")
        for item in self.cars:
            if item.title == title:
                if item.model == model:
                    self.cars.remove(item)
                    self.busy_car.append(item)
                    print("car busy")

    def delete_busy_car(self):
        title = input("title:")
        model = input("model:")
        for item in self.busy_car:
            if item.title == title and item.model == model:
                self.busy_car.remove(item)
                self.cars.append(item)
                print("succesful")

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


class Manager:
    def __init__(self):
        title = input("title: ")
        self.tp = Busy(title)

    def run(self):
        while True:
            print("""
====== MANAGER PANEL ======
1. Mashina qo‘shish
2. Hodim qo‘shish
3. Mashina o‘chirish
4. Hodim o‘chirish
5. Mavjud mashinalar ro‘yxati
6. Mavjud hodimlar ro‘yxati
7. Mashinani band qilish
8. Mashinani bekor qilish(agar band qilingan bolsa)
9. Band mashinalarni korish
10. Band hodimlarni ko‘rish
0. Chiqish
""")

            choice = input("Tanlang: ")

            if choice == "1":
                self.tp.add_car()
            elif choice == "2":
                self.tp.add_staff()
            elif choice == "3":
                self.tp.delete_car()
            elif choice == "4":
                self.tp.delete_staff()
            elif choice == "5":
                self.tp.view_car()
            elif choice == "6":
                self.tp.view_staff()
            elif choice == "7":
                self.tp.add_busy_car()
            elif choice == "8":
                self.tp.delete_busy_car()
            elif choice == "9":
                self.tp.view_busy_cars()
            elif choice == "10":
                self.tp.view_busy_staff()
            elif choice == "0":
                print("Dastur tugadi.")
                break
            else:
                print("Noto‘g‘ri tanlov")

manager = Manager()
manager.run()