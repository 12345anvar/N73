from crud.books import add_book
from crud.category import add_category, show_all_categories
from crud.user import login, validate, logout_all


def auth_menu():
    print("""
    1. Register
    2. Login
    3. Validate
    3. Exit
    """)
    option = input("Enter your option: ")
    if option == "1":
        return auth_menu()
    elif option == "2":
        if login():
            print("Welcome")
            return main()
        else:
            print("Invalid email or password")
            return auth_menu()
    elif option == "3":
        if validate():
            print("Welcome")
            return main()

    elif option == "4":
        print("Goodbye")
        return None
    else:
        print("Invalid option")
    return auth_menu()


def main():
    print("""
    1. Add category
    2. Delete category
    3. Show all category
    4. Show all books
    5. Add book
    6. Delete book
    7. Search book | name, author, note, category
    8. Exit
    """)
    option = input("Enter your option: ")
    if option == "1":
        add_category()
    elif option == "2":
        pass
    elif option == "3":
        show_all_categories()
    elif option == "4":
        pass
    elif option == "5":
        add_book()
    elif option == "6":
        pass
    elif option == "7":
        pass
    elif option == "8":
        print("Goodbye")
        return None
    else:
        print("Invalid option")
    return main()


if __name__ == '__main__':
    # execute_query(users)
    # execute_query(category)
    # execute_query(books)
    # execute_query(codes)
    logout_all()
    auth_menu()