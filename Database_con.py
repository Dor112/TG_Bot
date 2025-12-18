import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user = "postgres",
                              password = "A27032006",
                              host = "localhost",
                              port = "5432",
                              database = "TG_BOT")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = connection.cursor()

#cur.execute("INSERT INTO users (id) VALUES (%s)", ())
connection.commit()


