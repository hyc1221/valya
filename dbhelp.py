import sqlite3 as sql

con = sql.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS test(userid TEXT PRIMARY KEY,        
         name TEXT,
         balance INT,
         gender TEXT)""")
    #cur.execute("INSERT INTO `test` VALUES (404934560405782528, 1000)")
    cur.execute("SELECT * FROM `test`")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.commit()
    cur.close()

def newUser(id, name):
    values = [id, name, 1000, 'ХЗ']
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO test VALUES(?,?,?,?)", values)
        con.commit()
        cur.close()

def checkId(id):
    with con:
        cur = con.cursor()
        info = cur.execute("SELECT * FROM test WHERE userid=?", (id,))
        if info.fetchone() is None:
            cur.close()
            return False
        else:
            cur.close()
            return True

def setGender(id, gender):
    with con:
        cur = con.cursor()
        cur.execute('UPDATE test SET gender = ? WHERE userid = ?', (gender, id))
        con.commit()
        cur.close()

def checkGender(id):
    with con:
        cur = con.cursor()
        cur.execute("SELECT gender FROM test WHERE userid=?", (id,))
        result = cur.fetchone()
        cur.close()
        return result

def checkinfo(id):
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM test WHERE userid=?", (id,))
        result = cur.fetchone()
        cur.close()
        return result