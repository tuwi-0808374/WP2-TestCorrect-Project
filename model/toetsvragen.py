from model.database import Database

class Toetsvragen():
    def __init__(self):
        database = Database('./databases/database.db')
        self.cursor, self.con = database.connect_db()

    def getToetsvragen(self, start=0, limit=10):
        query = 'SELECT * FROM questions LIMIT ? OFFSET ?'
        result = self.cursor.execute(query, (limit, start)).fetchall()
        return result

    def getTotalQuestions(self):
        query = 'SELECT COUNT(*) FROM questions'
        total = self.cursor.execute(query).fetchone()[0]
        return total