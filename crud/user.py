from core.db_settings import execute_query
from utils.email_sending import generate_code, send_email


def register():
    email = input("Email: ")
    password = input("Password: ")

    # check email if exists or not
    # ask password twice
    query = "INSERT INTO users (email, password) VALUES (%s, %s)"
    params = (email, password)
    if execute_query(query=query, params=params):
        code = generate_code(user_email=email)
        if send_email(
                recipient_email=email, subject="Confirmation code",
                body=f"This is your code: {code}"
        ):
            print("Code sent to your email")
            if validate():
                return True
            return False
        else:
            print("Something went wrong, try again later")
            return False
    else:
        print("Something went wrong, try again later")
        return False


def validate():
    code = input("Code: ")
    query = "SELECT * FROM codes WHERE code = %s"
    params = (code,)
    user_code = execute_query(query=query, params=params, fetch="one")
    if user_code:
        query1 = "DELETE FROM codes WHERE code = %s"
        params1 = (code,)
        execute_query(query=query1, params=params1)

        query2 = "UPDATE users SET is_active=True WHERE email = %s"
        params2 = (user_code['email'],)
        execute_query(query=query2, params=params2)

        return True
    else:
        print("Invalid code")
        return validate()


def login():
    email = input("Email: ")
    password = input("Password: ")
    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    params = (email, password)
    if execute_query(query=query, params=params, fetch="one"):
        query2 = "UPDATE users SET is_login=True WHERE email = %s"
        params2 = (email,)
        execute_query(query=query2, params=params2)

        return True
    return False


def get_active_user():
    query = "SELECT * FROM users WHERE is_login=TRUE"
    return execute_query(query=query, fetch="one")


def logout_all():
    query1 = "UPDATE users SET is_login=False"
    execute_query(query=query1)