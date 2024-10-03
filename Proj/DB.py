from psycopg2 import OperationalError, connect


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    "learn_market", "postgres", "12qwaszx", "localhost", "5432"
)


