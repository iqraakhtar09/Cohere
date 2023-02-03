import psycopg2


def get_cursor():
    conn = psycopg2.connect(database="CohereChatBot",
                            host="localhost",
                            user="postgres",
                            password="password",
                            port="5432")
    return conn.cursor()
