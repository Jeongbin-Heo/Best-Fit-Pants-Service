import psycopg2

hostname = 'localhost'
database = 'jeongbinheo'
username = 'jeongbinheo'
pwd = 'wilshere10'
port_id = 5432

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS pants(
    Id INTEGER NOT NULL,
    Height INTEGER,
    Weight INTEGER,
    Color VARCHAR(50),
    Fit VARCHAR(50),
    Size INTEGER,
    PRIMARY KEY(Id)
)""")

conn.commit()


cur.close()
conn.close()