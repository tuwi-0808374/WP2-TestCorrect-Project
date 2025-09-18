import bcrypt

from model.database import Database

class User():
    def __init__(self):
        database = Database('./databases/database.db')
        self.cursor, self.con = database.connect_db()

    def get_users(self, search = None):
        if search:
            result = self.cursor.execute('SELECT * FROM users WHERE display_name LIKE ?', (f"%{search}%",)).fetchall()
        else:
            result = self.cursor.execute('SELECT * FROM users').fetchall()
        return result

    def get_users_offset(self, start, limit, search = None):
        if search:
            result = self.cursor.execute('SELECT * FROM users WHERE display_name LIKE ? LIMIT ? OFFSET ?', (f"%{search}%", limit, start)).fetchall()
        else:
            result = self.cursor.execute('SELECT * FROM users LIMIT ? OFFSET ?', (limit, start)).fetchall()
        return result

    def login_user(self, login, password):
        login_query = 'SELECT * FROM users WHERE login = ?LIMIT 1'

        user_row = self.cursor.execute(login_query, (login,)).fetchone()
        if user_row:
            stored_password = user_row['password']
            entered_password = password.encode('utf-8')
            same_password = bcrypt.checkpw(entered_password, stored_password)
            print(same_password)
            if same_password:
                return user_row

        return None


    def get_user(self, user_id):
        result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (str(user_id),)).fetchone()
        return result

    def create_user(self, login, password, display_name, is_admin):
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password, salt)

        self.cursor.execute(
            "INSERT into users (login, password, display_name, is_admin) VALUES (?, ?, ?, ?)",
            (login, hash, display_name, is_admin))
        self.con.commit()

        return True

    def update_user(self, user_id, login, password, display_name, is_admin):
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password, salt)

        self.cursor.execute(
            'UPDATE users SET login = ?, password = ?, display_name = ?, is_admin = ? WHERE user_id = ?',
            (login, hash, display_name, is_admin, user_id)
        )
        self.con.commit()

        return True

    def delete_user(self, user_id):
        print(user_id)
        self.cursor.execute("DELETE FROM users WHERE user_id = ?", (str(user_id),))
        self.con.commit()