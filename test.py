import psycopg2

try:
    db = psycopg2.connect("dbname='bookstore' user='postgres' host='localhost' password='Kiash987654' port='5432'")
    print('connection to database is successful')
except:
    print('connection to the database was unsuccessful')
    exit(1)

exit(0)
