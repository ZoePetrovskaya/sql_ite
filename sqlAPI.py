'''
import sqlite3 as sq
with sq.connect("cars.db") as con:

    cars = [ \
    ('Audi', 52642),      
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bently', 350000)]
    cur =con.cursor()'''
    #cur.execute("DROP TABLE IF EXISTS users")
'''    
    
    #cur.execute("""CREATE TABLE IF NOT EXISTS cars(  car_id INTEGER PRIMARY KEY AUTOINCREMENT, model TEXT NOT NULL, price INTEGER)""")
    

    # менеджер контекста with в конце выполняет con.commit() сохраняет изменения в базу данных  con.close() закрытие
    cur.execute("INSERT INTO cars VALUES(1,'Audi', 52642)")       
    cur.execute("INSERT INTO cars VALUES(2,'Mercedes', 57127)")
    cur.execute("INSERT INTO cars VALUES(3,'Skoda', 9000)")
    cur.execute("INSERT INTO cars VALUES(4,'Volvo', 29000)")
    cur.execute("INSERT INTO cars VALUES(5,'Bently', 350000)")'''

    # вместо этого
    #for car in cars:
    #    cur.execute("INSERT INTO cars VALUES(null, ?, ?)", car)

    # вмсто этого cur.executemany с неименованными параметрами ? , ?

    #cur.executemany("INSERT INTO cars VALUES(null, ?, ?)", cars)

    # еще способ: именованные параметры
    # вместо :Price запишется значение из словаря с ключом 'Price'
    # А%  - все автомобили с названием начинающимся на А
    #cur.execute("UPDATE cars SET price = :Price Where model like 'A%' ", {'Price': 25000})

    # несколько запросов подряд cur.executescript()
    
    #cur.executescript("DELETE FROM cars WHERE model LIKE 'A%';         UPDATE cars SET  price = price + 1000")

'''result = cur.fetchall()

    #print(result)
    for x in result:
        print("запись",x)'''


#  через try
# BEGIN к этому состоянию база откатится, если  произойдет ошибка
'''
import sqlite3 as sq

con = None
try:

    con = sq.connect("cars.db")
    cur = con.cursor()
    cur.executescript("     CREATE TABLE IF NOT EXISTS cars(\
        car_id INTEGER PRIMARY KEY AUTOINCREMENT, \
        model TEXT NOT NULL,\
        price INTEGER); \
     \
    BEGIN;  \
    INSERT INTO cars VALUES(NULL,'Audi', 52642);     \
    INSERT INTO cars VALUES(NULL,'Mercedes', 57127); \
    INSERT INTO cars VALUES(NULL,'Skoda', 9000); \
    INSERT INTO cars VALUES(NULL,'Volvo', 29000); \
    INSERT INTO cars VALUES(NULL,'Bently', 350000);  \
    UPDATE cars SET  price = price + 1000 \
     ")
    
    con.commit()


except sq.Error as e:
    if con:
        con.rollback() # метод отката в состоянии BEGIN
        print("Ошибка в выполнении запроса")

finally:
    if con:
        con.close()
'''
# связь двух таблиц
import sqlite3 as sq
with sq.connect("cars.db") as con:
    #con.row_factory = sq.Row # в результате будет создаваться словарь, а не кортеж
    cur =con.cursor()
    
    cur.executescript(""" CREATE TABLE IF NOT EXISTS cars( \
      car_id INTEGER   PRIMARY KEY AUTOINCREMENT, 
      model TEXT NOT NULL, \
      price INTEGER); \
      CREATE TABLE IF NOT EXISTS cust( \
      name TEXT, \
      tr_in INTEGER, \
      buy INTEGER); \
      """)
    cur.execute("INSERT INTO cars VALUES (NULL, 'Запорожец', 1000)")
    last_row_id = cur.lastrowid # свойстро будет содержать id последней записи

    



    buy_car_id = 2
    cur.execute("INSERT INTO cust VALUES('Федор', ?, ?)", (last_row_id, buy_car_id))

# такая манипуляция позволяет вносить по id последнего внесения в другую базу
    cur.execute("SELECT * from cars")
    result = cur.fetchall()

    #print(result)
    #for x in result:
      #  print("запись",x)
    #print(result['model'], result['price'])


