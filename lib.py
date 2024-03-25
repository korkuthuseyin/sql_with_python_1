import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname='korkut',
        user='postgres',
        password='yzv322e',
        host='127.0.0.1',
        port='5432'
    )
    cur = conn.cursor()
    return conn, cur

def close_db(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

def create_table(tablename):
    conn, cur = connect_db()
    cur.execute(f'CREATE TABLE {tablename} (id SERIAL PRIMARY KEY, name VARCHAR(50), barcode VARCHAR(50))')
    close_db(conn, cur)
    
def insert_data(tablename, name, barcode):
    conn, cur = connect_db()
    cur.execute(f"SELECT MAX(id) FROM {tablename}")
    last_id = cur.fetchone()[0]
    if last_id is not None:
        next_id = last_id + 1
    else:
        next_id = 1
    
    cur.execute(f"INSERT INTO {tablename} (id, name, barcode) VALUES ('{next_id}', '{name}', '{barcode}')")
    close_db(conn, cur)