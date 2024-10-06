# Импорт взаимодествия с sql
import psycopg2
# Импорт конфигурации для соединения с БД
from config import db_name, user, password, host

# Функция показать все использует print, так как для удобства был использован цикл
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

# Фнкция показать отдельные элемнеты, нужно sql запрос прописывать вручную и используется print
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

# Функция запрос для изменений в БД, результат не возвращает, через print возвращает Done
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


# Функция вернуть резукльтат, требуется чтобы добавлять в корзину, испульзуется return
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




