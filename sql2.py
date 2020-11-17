import sqlite3 as sq
with sq.connect("saper.db") as con:
    cur =con.cursor()
    #cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users(\
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,\
        sex INTEGER NOT NULL DEFAULT 1,\
        old INTEGER,\
        score INTEGER)""")
   

    '''cur.execute("SELECT name, old FROM users \
        WHERE old > 3\
        ORDER by old DESC\
        LIMIT 2,3 ")'''
    #cur.execute("select * from users")
    #cur.execute("select count(score) as count from games Where user_id =1")
    #cur.execute("select sum(score) as sum , user_id from games  group by user_id order by sum desc")
    #cur.execute("SELECT name, sex, games.score FROM games join users on games.row_id =users.user_id")# сводный отчет   
    #cur.execute("SELECT name, sex, games.score from users, games")#просто набор данных
    '''cur.execute("select name, sex, sum(games.score) as score from games\
       join users on  games.row_id =users.user_id  \
          group by user_id \
          order by score desc")'''
    #cur.execute('SELECT score, "from" from tab1 UNION SELECT val, type from tab2') # Unionоставляет только уникальные значения score сопоставляется val, а from сопоставляется type
    #cur.execute('SELECT score from tab1 UNION SELECT val from tab2') 
    #cur.execute("Update tab1 set 'from' ='tab1'")

    # вложенные запросы
    #cur.execute(' SELECT subject, mark from marks WHERE id =2 and subject like "Химия"')

    #SELECT name, subject, mark from marks join students on students.rowid = marks.id where mark > 3 and subject like "Химия"')
    # выбираем столбцы имя предмет и оценка из таблицы оценки, обьединенной с таблицей студенты по совпадению id и доп условие
    
    # объединяем оба запроса
    '''
    cur.execute('SELECT name, subject, mark    \
        from marks join students on students.rowid = marks.id \
                where mark > (SELECT mark from marks WHERE id =2 and subject like "Химия") and subject like "Химия"')'''

    #cur.execute('insert into female  SELECT null, name, sex, old from students where sex = 2')

    #cur.execute('UPDATE marks set mark = 3 WHERE mark <= (SELECT min(mark) from marks where id = 2)') # пишет, что база заблокирована


    result = cur.fetchall()

    #print(result)
    for x in result:
        print("запись",x)


     
