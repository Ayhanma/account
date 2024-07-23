import sqlite3 as sql
con = sql.connect('project.db')
cur = con.cursor()
class Data_Base():
    def __init__(self, inc, out, month):
        self.inc = inc
        self.out = out
        self.month = month
    def add(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS data( 
                    id INTEGER PRIMARY KEY, 
                    month TEXT, 
                    income INTEGER, 
                    outcome INTEGER, 
                    substraction INTEGER
                    );
                    ''')
        sub = self.inc - self.out
        cur.execute('INSERT INTO data (month, income, outcome, substraction) VALUES (?, ?, ?, ?)',(self.month, self.inc, self.out, sub))
        con.commit()
    def read(self,id=None):
        if id == None:
            cur.execute("SELECT * FROM data WHERE month = ?", (self.month,))
        else:
            cur.execute("SELECT * FROM data WHERE id = ?", (id,))
        
        print(cur.fetchall())