from model.database import Database

class Toetsvragen():
    def __init__(self):
        database = Database('./databases/database.db')
        self.cursor, self.con = database.connect_db()

    def getToetsvragen(self):
        result = self.cursor.execute('SELECT * FROM questions').fetchall()
        print(result)
        return result