from core.db_settings import execute_query
from crud.category import show_all_categories


def add_book():
    if show_all_categories() is None:
        return None
    category_id = input("Enter category id: ")
    # check this id is existing or not

    name = input("Enter book name: ")
    author = input("Enter book author: ")
    note = input("Enter note: ")
    status = input("Enter book status(done,ongoing,new): ")
    query = "INSERT INTO books (category_id, name, author, note, status) VALUES (%s, %s, %s, %s, %s)"
    params = (category_id, name, author, note, status,)
    if execute_query(query=query, params=params):
        print("Books is added")
        return None
    else:
        print("Something getting wrong, please try again later")
        return True


def delete_book(cursor, conn):
    name  = input("Enter book name: ")
    query = "DELETE FROM books WHERE name = %s"
    params = (name,)
    cursor.execute(query, params)
    conn.commit()


def search_book(cursor, conn):
    """Search with name, author, note"""
    search_term = input("Enter search term (name, author or note): ").strip()

    query = """
    SELECT * FROM books
    WHERE name ILIKE %s
       OR author ILIKE %s
       OR note ILIKE %s
    LIMIT 20
    """

    search_pattern = f"%{search_term}%"
    params = (search_pattern, search_pattern, search_pattern)

    cursor.execute(query, params)
    results = cursor.fetchall()

    return results


def show_all_books():
    query = "SELECT * FROM category;"
    books = execute_query(query=query, fetch="all")
    if books:
        counter = 1
        for book in books:
            print(f"{counter}) {book['name']}\t{book['author']}\t{book['note']}\t{book['status']}")
            counter += 1
        return True

    else:
        print("No books found")
        return None
