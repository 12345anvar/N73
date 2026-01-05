from core.db_settings import execute_query
from core.tables import books, category



def main():
    pass

if __name__ == "__main__":
    execute_query(category)
    execute_query(books)
    main()