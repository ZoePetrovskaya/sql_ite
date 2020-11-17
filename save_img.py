# хранение изображений
import sqlite3 as sq

def readAva(n): # n- номер аватарки
    try:
        with open(f"avas/{n}.png","rb") as f: # аватарка хранится в виде avas/1.png
            return f.read()
    except IOError as e:
        print(e)
        return False

def writeAva(name, data): # записываем этоизображение
        try:
            with open(name, "wb") as f:
                f.write(data)
        except IOError as e:
            print(e)
            return False
     
        return True


with sq.connect("cars.db") as con:
    con.row_factory = sq.Row
    cur =con.cursor()

    #cur.execute(""" CREATE TABLE IF NOT EXISTS users( name TEXT ,  ava BLOB,   score INTEGER) """)
    cur.executescript("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    ava BLOB,
    score INTEGER)
""")
    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()['ava']

    img = readAva(1) #читаем аватарку и если успешно, то 
    if img:
        binary = sq.Binary(img) # преобразовываем  бинарные данные img  в бинарный объект SQLite
        cur.execute("INSERT INTO users VALUES ('Николай', ?, 1000)", (binary,))

    
    writeAva("out.png", img)





    


'''    cur.execute(" SELECT model, price From cars")'''