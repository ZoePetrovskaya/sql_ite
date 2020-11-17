# создание бэкапа БД

import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()
 
for sql in con.iterdump(): # получаем список запросов для форимирования БД
     print(sql)

# лучше через cmd



''' выведется история запросов
    BEGIN TRANSACTION;
CREATE TABLE cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER);
INSERT INTO "cars" VALUES(1,'Audi',0);
INSERT INTO "cars" VALUES(2,'Mercedes',57127);
INSERT INTO "cars" VALUES(3,'Skoda',9000);
INSERT INTO "cars" VALUES(4,'Volvo',29000);
INSERT INTO "cars" VALUES(5,'Bentley',350000);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('cars',5);
CREATE TABLE users (
            name TEXT,
            ava BLOB,
            score INTEGER);
INSERT INTO "users" VALUES('Николай', …,1000);
COMMIT;
'''
# запишем их в файл
with open("sql_damp.sql", "w") as f:
    for sql in con.iterdump():
        f.write(sql)

# допустим база слетела
with open("sql_damp.sql", "r") as f:
    sql = f.read()
    cur.executescript(sql)

'''
# создание базы в памяти
data = [("car", "машина"), ("house", "дом"), ("tree", "дерево"), ("color", "цвет")]
 
con = sq.connect(':memory:')
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dict(
        eng TEXT, rus TEXT    
    )""")
 
    cur.executemany("INSERT INTO dict VALUES(?,?)", data)
 
    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())
    '''