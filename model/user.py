from model.database import Database

class User():
    def __init__(self):
        database = Database('./databases/database.db')
        self.cursor, self.con = database.connect_db()

    def get_users(self):
        result = self.cursor.execute('SELECT * FROM users').fetchall()
        return result

    def get_user(self, user_id):
        result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (str(user_id))).fetchone()
        return result

