import psycopg2


def test_connection():
    try:
        db = psycopg2.connect("dbname='bookstore' user='postgres' host='localhost' password='Kiash987654' port='5432'")
        print('connection to database is successful')
    except:
        print('connection to the database was unsuccessful')
        exit(1)

    exit(0)


def create_table():
    conn = psycopg2.connect("dbname='bookstore' user='postgres' host='localhost' password='Kiash987654' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='bookstore' user='postgres' host='localhost' password='Kiash987654' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='bookstore' user='postgres' host='localhost' password='Kiash987654' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='bookstore' user='postgres' host='localhost' password='Kiash987654' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='bookstore' user='postgres' host='localhost' password='Kiash987654' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE bookstore SET quantity=%s, price=%s WHERE ITEM=%s", (quantity, price, item,))
    conn.commit()
    conn.close()


test_connection()
#create_table()
#insert("Beer Mug", 20, 10)
#update(10, 20, "wine glass")
#delete("Tea Mug")
print(view())