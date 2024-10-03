import psycopg2
from config import db_name, user, password, host

def show_all():
    try:
        connection = psycopg2.connect(database=db_name,
                user=user,
                password=password,
                host=host,
                )
        connection.autocommit = True
    
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM market;')
            for i in cursor.fetchall():
                print(i)
        
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PstgtreSQL connection close')



show_all()