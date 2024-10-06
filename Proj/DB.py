import psycopg2
from config import db_name, user, password, host


def show_all():
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM market;")
            print(("Номер", "Название", "Описание", "Цена", "Количество"))
            for i in cursor.fetchall():
                print(i)

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PstgtreSQL connection close")


def show_any(query):
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(query)
            for i in cursor.fetchall():
                print(i)

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PstgtreSQL connection close")


def query(query):
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(query)
            print('Done')

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PstgtreSQL connection close")


def return_result(query):
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=user,
            password=password,
            host=host,
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PstgtreSQL connection close")

#query('Update market SET price = 51000 where product_id = 1')


