import sqlite3 as sq

cars = [ \
    ('Audi', 52642),      
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bently', 350000)]
    

with sq.connect("cars.db") as con:
    con.row_factory = sq.Row # в результате будет создаваться запись <sqlite3.Row object at 0x000001C5612C54B0>
    cur =con.cursor()
    
    cur.executescript(""" CREATE TABLE IF NOT EXISTS cars( \
      car_id INTEGER   PRIMARY KEY AUTOINCREMENT, 
      model TEXT NOT NULL, \
      price INTEGER); \
      """)
    #cur.executemany("INSERT INTO cars VALUES (NULL, ?, ?)", cars)

    cur.execute("SELECT model, price from cars")
    #result = cur.fetchall()
    #print("fetchall", result)

    #result_many = cur.fetchmany(4)
    #print("fetchmany:", result_many)
    

    for x in cur: # экономия пямяти
        #print("запись",x)
        print(x['model'], x['price'])
  
    

    # хранение изображений
    
   